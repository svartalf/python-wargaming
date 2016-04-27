import os
import json
import requests

from wargaming.exceptions import APIError, RequestError, ValidationError


class WGAPI(object):
    """Result from WG API request"""

    def __init__(self, url, **kwargs):
        self.url = url
        for name, value in kwargs.items():
            if isinstance(value, list):
                kwargs[name] = ','.join(value)
        self.params = kwargs
        self.data = None
        self._iter = None

    def _fetch_data(self):
        if not self.data:
            self.response = response = requests.get(self.url, params=self.params, headers={
                'User-Agent': 'settings.HTTP_USER_AGENT_HEADER',
            }).json()

            if response['status'] == 'error':
                error = response['error']
                raise RequestError(**error)

            self.data = response['data']
        return self.data

    def __len__(self):
        return len(self._fetch_data())

    def __str__(self):
        return self._fetch_data()

    def __unicode__(self):
        return self._fetch_data()

    def __iter__(self):
        return self

    def next(self):
        self._fetch_data()
        if not self._iter:
            self._iter = iter(self.data)
        return next(self._iter)

    def __getitem__(self, item):
        self._fetch_data()
        return self.data[item]

    def __repr__(self):
        return "<WGAPI: %s>" % self.url


class MetaAPI(type):
    """MetaClass Loads current scheme from schema.json file
    and creates API structure based on scheme.

    Scheme format:
    {'module_name': {                         # account, globalmap, etc
        'function_name': {                    # list, provinces, etc
            '__doc__': description,           # text description
            'parameter': 'type of parameter'  # allowed parameters
        }
    }}
    """

    def __new__(cls, name, bases, attrs):
        new_cls = super(MetaAPI, cls).__new__(cls, name, bases, attrs)
        new_cls._module_dict = {}

        def init_game(self, application_id, language='ru',
                base_url='https://api.worldoftanks.ru/%s/' % name.lower()):
            """__init__ used for global name space
                :param application_id: Application ID
                :
            """
            self._application_id = application_id
            self._language = language
            self._base_url = base_url

            for k, v in self._module_dict.items():
                setattr(self, k, v(application_id, language, base_url))

        def init_module(self, application_id, language='ru',
                base_url='https://api.worldoftanks.ru/%s/' % name.lower()):
            self._application_id = application_id
            self._language = language
            self._base_url = base_url

        def make_api_call(url, fields):
            doc = fields.pop('__doc__')
            def api_call(self, **kwargs):
                for field in kwargs.keys():
                    if field not in fields:
                        raise ValidationError('Wrong parameter: {0}'.format(field))

                if 'language' not in kwargs:
                    kwargs['language'] = self._language

                if 'application_id' not in kwargs:
                    kwargs['application_id'] = self._application_id

                return WGAPI(self._base_url + url, **kwargs)
            doc += "\n\nKeyword arguments:\n"
            for name, value_desc in fields.items():
                doc += "%-20s  doc:      %s\n" % (name, value_desc['doc'])
                doc += "%-20s  required: %s\n" % ('', value_desc['required'])
                doc += "%-20s  type:     %s\n\n" % ('', value_desc['type'])
            api_call.__doc__ = doc
            api_call.__name__ = str(url.split('/')[-1])
            api_call.__module__ = str(url.split('/')[0])
            return api_call

        new_cls.__init__ = init_game

        base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'schema')
        source_file = os.path.join(base_dir, '%s-schema.json' % name.lower())
        for obj_name, obj in json.load(open(source_file)).items():
            obj_full_name = "%s.%s" % (name, obj_name)
            new_cls._module_dict[obj_name] = type(str(obj_full_name), (), {})

            module_obj = new_cls._module_dict[obj_name]
            module_obj.__init__ = init_module

            for func_name, func in obj.items():
                setattr(module_obj, func_name, make_api_call(obj_name + '/' + func_name + '/', func))

        return new_cls
