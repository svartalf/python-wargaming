import os
import json
import requests
import six
from retrying import retry
from datetime import datetime

from wargaming.exceptions import RequestError, ValidationError
from wargaming.settings import ALLOWED_GAMES, ALLOWED_REGIONS, HTTP_USER_AGENT_HEADER, RETRY_COUNT


def check_allowed_game(game):
    if game not in ALLOWED_GAMES:
        raise ValidationError("Game '%s' is not allowed list: %s" %
                              (game, ', '.join(ALLOWED_GAMES)))


def check_allowed_region(region):
    if region not in ALLOWED_REGIONS:
        raise ValidationError("Region %s is not allowed list: %s" %
                              (region, ', '.join(ALLOWED_REGIONS)))


def region_url(region, game):
    check_allowed_game(game)
    check_allowed_region(region)

    # all api calls for all project goes to api.worldoftanks.*
    # maybe WG would move this api to api.wargaming.net
    return 'https://api.worldoftanks.%s/%s/' % (region, game)


@six.python_2_unicode_compatible
class WGAPI(object):
    """Result from WG API request"""

    def __init__(self, url, stop_max_attempt_number=RETRY_COUNT, **kwargs):
        self.url = url
        for name, value in kwargs.items():
            if isinstance(value, list) or isinstance(value, tuple):
                kwargs[name] = ','.join(str(i) for i in value)
            elif isinstance(value, datetime):
                kwargs[name] = value.isoformat()
        self.params = kwargs
        self._data = None
        self.error = None
        self._iter = None
        self.stop_max_attempt_number = stop_max_attempt_number
        self._fetch_data = retry(
            stop_max_attempt_number=stop_max_attempt_number,
            retry_on_exception=lambda ex: isinstance(ex, RequestError)
        )(self._fetch_data)

    def _fetch_data(self):
        if not self._data:
            self.response = response = requests.get(self.url, params=self.params, headers={
                'User-Agent': HTTP_USER_AGENT_HEADER,
            }).json()

            if response.get('status', '') == 'error':
                self.error = response['error']
                raise RequestError(**self.error)

            self._data = response.get('data', response)
        return self._data

    @property
    def data(self):
        return self._fetch_data()

    @data.setter
    def data(self, value):
        """setter is used if needed to fake response or reset data"""
        self._data = value

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def __iter__(self):
        return iter(self.data)

    def keys(self):
        return self.data.keys()

    def items(self):
        return self.data.items()

    def values(self):
        return self.data.values()

    def __getitem__(self, item):
        """__getitem__ with smart type detection
        would try to lookup data['123']
        if not found would try data[123] and vise versa
        """
        data = self.data
        try:
            return data[item]
        except KeyError:
            item = int(item) if type(item) == str and item.isdigit() else str(item)
            return data[item]

    def __repr__(self):
        res = str(self.data)
        return res[0:200] + ('...' if len(res) > 200 else '')


class ModuleAPI(object):
    _module_dict = {}

    def __init__(self, application_id, language, base_url):
        """
        :param application_id: WG application id
        :param language: default language param
        :param base_url: base url of module api
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

                for field, params in fields.items():
                    if params['required'] and field not in kwargs:
                        raise ValidationError('Missing required paramter : {0}'.format(field))

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

        # check if values are correct
        check_allowed_game(name.lower())

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
