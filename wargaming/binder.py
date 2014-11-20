# -*- coding: utf-8 -*-

import datetime

import requests
from six.moves.urllib.parse import urlparse, urlunparse, urlencode

from wargaming import settings
from wargaming.exceptions import RequestError
from wargaming.api import BaseAPI, SubclassAPI

__all__ = ('bind',)


def __init__(self, parent):
    if isinstance(parent, SubclassAPI):
        self.api = parent.api
    else:
        self.api = parent


def execute(self, **kwargs):
    # Build GET parameters for query
    parameters = {}

    for key, value in kwargs.items():
        if value is None:
            continue

        prepare_func = getattr(self.api, 'prepare_{0}'.format(key), None)
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
        'application_id': self.api.application_id,
    })

    if 'language' not in parameters:
        parameters['language'] = self.api.language

    url = self.api._get_url(self.path, parameters)

    response = requests.get(url, headers={
        'User-Agent': settings.HTTP_USER_AGENT_HEADER,
    }).json()

    if response['status'] == 'error':
        raise RequestError(**response['error'])

    return response['data']


def bind(**config):
    docstring = config.pop('doc', None)

    properties = {
        'path': config['path'],
        'allowed_params': config['allowed_params'],
        '__init__': __init__,
        'execute': execute,
    }

    cls = type('API{0}Method'.format(config['path'].title().replace('/', '')),
               (object, ), properties)

    def _call(self, **kwargs):
        return cls(self).execute(**kwargs)

    _call.__name__ = config['path'].strip('/').replace('/', '_').lower()
    if docstring is not None:
        _call.__doc__ = docstring

    return _call
