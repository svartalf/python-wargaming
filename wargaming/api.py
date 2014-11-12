# -*- coding: utf-8 -*-

from six.moves.urllib.parse import urlparse, urlunparse, urljoin, urlencode

from wargaming import settings
from wargaming.exceptions import ValidationError


class MetaAPI(type):

    def __new__(cls, name, bases, attrs):
        attrs['_subclasses'] = {}
        new_cls = super(MetaAPI, cls).__new__(cls, name, bases, attrs)

        for name, sub_api in attrs.items():
            if not isinstance(sub_api, SubclassAPI):
                continue

            new_cls._subclasses[name] = sub_api

        return new_cls


class BaseAPI(object):
    _subclasses = None

    def __init__(self, application_id, base_url):
        self.application_id = application_id

        url_parts = urlparse(base_url)
        self.url_scheme = url_parts.scheme
        self.url_netloc = url_parts.netloc
        self.url_path = url_parts.path

        for subclass in self._subclasses.values():
            subclass.api = self

    def _get_url(self, path, parameters):
        return urlunparse([
            self.url_scheme,
            self.url_netloc,
            urljoin(self.url_path, path),
            None,
            urlencode(parameters),
            None
        ])

    @staticmethod
    def prepare_language(value):
        """Localization language

        One of the :data:`wargaming.settings.ALLOWED_LANGUAGES`
        """

        if value not in settings.ALLOWED_LANGUAGES:
            raise ValidationError('Invalid language: {0}'.format(value))

        return value

    @staticmethod
    def prepare_fields(value):
        """List of response fields

        Fields are separated by commas. Nested fields are separated by dots."""

        if value:
            return ','.join(value)

        return ''


class SubclassAPI(object):
    """Base class for all of the API endpoint 'namespaces'"""

    def __init__(self):
        self.api = None
