import os
import json
import requests
from retrying import retry

from wargaming.exceptions import RequestError, ValidationError
from wargaming.settings import ALLOWED_GAMES, ALLOWED_REGIONS, HTTP_USER_AGENT_HEADER


def region_url(region, game):
    if game not in ALLOWED_GAMES:
        raise ValidationError("Game '%s' is not allowed list: %s" %
                              (game, ', '.join(ALLOWED_GAMES)))

    if region not in ALLOWED_REGIONS:
        raise ValidationError("Region %s is not allowed list: %s" %
                              (region, ', '.join(ALLOWED_REGIONS)))

    # all api calls for all project goes to api.worldoftanks.*
    # maybe WG would move this api to api.wargaming.net
    return 'https://api.worldoftanks.%s/%s/' % (region, game)


class WGAPI(object):
    """Result from WG API request"""

    def __init__(self, url, stop_max_attempt_number=10, **kwargs):
        self.url = url
        for name, value in kwargs.items():
            if isinstance(value, list):
                kwargs[name] = ','.join(str(i) for i in value)
        self.params = kwargs
        self.data = None
        self._iter = None
        self.stop_max_attempt_number = stop_max_attempt_number
        self._fetch_data = retry(stop_max_attempt_number=stop_max_attempt_number)(self._fetch_data)

    def _fetch_data(self):
        if not self.data:
            self.response = response = requests.get(self.url, params=self.params, headers={
                'User-Agent': HTTP_USER_AGENT_HEADER,
            }).json()

            self.data = response.get('data', response)

            if response.get('status', '') == 'error':
                error = response['error']
                raise RequestError(**error)

        return self.data

    def __len__(self):
        return len(self._fetch_data())

    def __str__(self):
        return str(self._fetch_data())

    def __unicode__(self):
        return str(self._fetch_data())

    def __iter__(self):
        return self

    def next(self):
        self._fetch_data()
        if not self._iter:
            self._iter = iter(self.data)
        return next(self._iter)
    # python 3.x
    __next__ = next

    def __getitem__(self, item):
        data = self._fetch_data()
        if item not in data:
            if type(item) == int:
                item = str(item)
            else:
                try:
                    item = int(item)
                except ValueError:
                    pass
        return data[item]

    def __repr__(self):
        res = str(self._fetch_data())
        return res[0:200] + ('...' if len(res) > 200 else '')


class ModuleAPI(object):
    _module_dict = {}

    def __init__(self, application_id, language, base_url):
        """
        :param application_id: WG application id
        :param language: default language param
        :param region: game geo region short name
        """
        self.application_id = application_id
        self.language = language
        self.base_url = base_url


class BaseAPI(object):
    _module_dict = {}

    def __init__(self, application_id, language, region):
        """
        :param application_id: WG application id
        :param language: default language param
        :param region: game geo region short name
        """
        self.application_id = application_id
        self.language = language
        self.region = region
        self.base_url = region_url(region, self.__class__.__name__.lower())
        for k, v in self._module_dict.items():
            setattr(self, k, v(application_id, language, self.base_url))


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

    def __new__(mcs, name, bases, attrs):
        cls = super(MetaAPI, mcs).__new__(mcs, name, bases, attrs)
        cls._module_dict = {}

        def make_api_call(url, fields):
            """
            API function generator (list, info, etc.)
            :param url: url to function
            :param fields:  allowed fields
            :return: api call function
            """
            doc = fields.pop('__doc__')

            def api_call(self, **kwargs):
                """API call to WG public API
                :param self: instance of sub module
                :param kwargs: params to WG public API
                :return: WGAPI instance
                """
                for field in kwargs.keys():
                    if field not in fields:
                        raise ValidationError('Wrong parameter: {0}'.format(field))

                if 'language' not in kwargs:
                    kwargs['language'] = self.language

                if 'application_id' not in kwargs:
                    kwargs['application_id'] = self.application_id

                return WGAPI(self.base_url + url, **kwargs)
            doc += "\n\nKeyword arguments:\n"
            for value_name, value_desc in fields.items():
                doc += "%-20s  doc:      %s\n" % (value_name, value_desc['doc'])
                doc += "%-20s  required: %s\n" % ('', value_desc['required'])
                doc += "%-20s  type:     %s\n\n" % ('', value_desc['type'])
            api_call.__doc__ = doc
            api_call.__name__ = str(url.split('/')[-1])
            api_call.__module__ = str(url.split('/')[0])
            return api_call

        # Loading schema from file
        base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'schema')
        source_file = os.path.join(base_dir, '%s-schema.json' % name.lower())
        schema = json.load(open(source_file))

        # Creating objects for class
        for obj_name, obj in schema.items():
            # make object name
            obj_full_name = "%s.%s" % (name, obj_name)
            # save module to _module_dict for initialization on class creation
            cls._module_dict[obj_name] = module_obj = type(str(obj_full_name), (ModuleAPI, ), {})

            # make this work without class initialization
            setattr(cls, obj_name, module_obj)

            for func_name, func in obj.items():
                setattr(module_obj, func_name, make_api_call(obj_name + '/' + func_name + '/', func))

        return cls
