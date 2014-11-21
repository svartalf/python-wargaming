# -*- coding: utf-8 -*-

import sys
import datetime

import requests
import six
from six.moves.urllib.parse import urlparse, urlunparse, urljoin, urlencode

from wargaming import settings
from wargaming.exceptions import ValidationError, RequestError


class MetaAPI(type):

    def __new__(cls, name, bases, attrs):
        module = attrs.pop('__module__')

        new_cls = super(MetaAPI, cls).__new__(cls, name, bases, {
            '__module__': module,
            'subclasses': {},
        })

        for k, v in attrs.items():
            if not isinstance(v, SubclassAPI):
                setattr(new_cls, k, v)
            else:
                new_cls.subclasses[k] = v

        return new_cls


class BaseAPI(object):

    def __init__(self, application_id, language=settings.DEFAULT_LANGUAGE,
                 base_url=''):

        self.application_id = application_id
        self.language = language

        url_parts = urlparse(base_url)
        self.url_scheme = url_parts.scheme
        self.url_netloc = url_parts.netloc
        self.url_path = url_parts.path

        for name, subclass in self.subclasses.items():
            subclass.contribute_to_class(self)
            setattr(self, name, subclass)

    def _get_url(self, path, parameters):
        return urlunparse([
            self.url_scheme,
            self.url_netloc,
            urljoin(self.url_path, path),
            None,
            urlencode(parameters),
            None
        ])

    def _request(self, path, **kwargs):
        parameters = {}

        for key, value in kwargs.items():
            if value is None:
                continue

            prepare_func = getattr(self, 'prepare_{0}'.format(key), None)
            if prepare_func is not None:
                value = prepare_func(value)

            if isinstance(value, (list, tuple)):
                value = ','.join([str(x) for x in value])
            elif isinstance(value, bool):
                value = int(value)
            elif isinstance(value, datetime.datetime):
                value = value.date().isoformat()
            elif isinstance(value, datetime.date):
                value = value.isoformat()

            parameters[key] = value

        parameters.update({
            'application_id': self.application_id,
        })

        if 'language' not in parameters:
            parameters['language'] = self.language

        url = self._get_url(path, parameters)

        response = requests.get(url, headers={
            'User-Agent': settings.HTTP_USER_AGENT_HEADER,
        }).json()

        if response['status'] == 'error':
            raise RequestError(**response['error'])

        return response['data']

    @staticmethod
    def prepare_language(value):
        """Localization language

        One of the :data:`wargaming.settings.ALLOWED_LANGUAGES`
        """

        if value not in settings.ALLOWED_LANGUAGES:
            raise ValidationError('Invalid language: {0}'.format(value))

        return value


class SubclassAPI(object):
    """Base class for all of the API endpoint 'namespaces'"""

    def __init__(self):
        self.api = None

    def contribute_to_class(self, instance):
        self.api = instance


def bind(path, allowed_params=(), doc=None):
    """Make a API method callable for class inherited from :class:`SubclassAPI`

    :param path: API endpoint path, relative to game base url
    :type path: str
    :param allowed_params: Allowed parameters names
    :type allowed_params: list | tuple
    :param doc: docstring for method callable
    :type doc: str | unicode
    """

    def request(self, **kwargs):
        for param in kwargs.keys():
            if param not in allowed_params:
                raise ValidationError('Wrong parameter: {0}'.format(param))

        return self.api._request(path, **kwargs)

    method_name = path.strip('/').replace('/', '_').lower()
    request.__name__ = method_name

    if doc is not None:
        # Creating proper docstring based on the `doc` and `allowed_params`
        # Also creating a dumb usage example. Just for case.

        docstring = six.StringIO()
        for line in doc.strip().splitlines():
            docstring.write(line.strip())
            docstring.write('\n')
        docstring.write('\n')
        for param in allowed_params:
            docstring.write(':param {0}:\n'.format(param))

        request.__doc__ = docstring.getvalue()

    return request
