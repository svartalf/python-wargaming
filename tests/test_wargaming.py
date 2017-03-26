import unittest
import six
import json
from datetime import datetime
from mock import patch, mock_open

from wargaming import WoT, WGN, WoTB, WoWP, WoWS, WoTX, settings
from wargaming.meta import MetaAPI, BaseAPI, WGAPI
from wargaming.settings import RETRY_COUNT, HTTP_USER_AGENT_HEADER
from wargaming.exceptions import ValidationError, RequestError

open_schema = mock_open(read_data=json.dumps(
    {'sub_module_name': {
        'func1': {
            'description': 'doc example for func1',
            'parameters': [{
                'name': 'application_id',
                'description': 'doc for application_id',
                'required': True,
                'type': 'string',
            }, {
                'name': 'language',
                'description': 'doc for language',
                'required': True,
                'type': 'string',
            }],
            'fields': [{
                'name': ['integer'],
                'type': 'numeric',
            }, {
                'name': ['timestamp'],
                'type': 'timestamp',
            }],
            'url': 'sub_module_name/func1',
        }, 'func2': {
            'description': 'doc example for func2',
            'parameters': [{
                'name': 'application_id',
                'description': 'doc for application_id',
                'required': True,
                'type': 'string',
            }, {
                'name': 'language',
                'description': 'doc for language',
                'required': True,
                'type': 'string',
            }, {
                'name': 'date',
                'description': 'sample date field',
                'type': 'timestamp/date',
            }, {
                'name': 'fields',
                'description': 'doc for fields',
                'type': 'string',
            }],
            'url': 'sub_module_name/func2',
        },
        # }, 'func3': { is used for custom function
        'func4': {
            'description': 'doc example for func4',
            'parameters': [{
                'name': 'application_id',
                'description': 'doc for application_id',
                'required': True,
                'type': 'string',
            }, {
                'name': 'language',
                'description': 'doc for language',
                'required': True,
                'type': 'string',
            }, {
                'name': 'clan_id',
                'description': 'fetch info about clan',
                'required': True,
                'type': 'string',
            }],
            'url': 'sub_module_name/func4',
        }

    }}
))


@patch('wargaming.meta.ALLOWED_GAMES', ['demo'])
@patch('wargaming.meta.GAME_API_ENDPOINTS', {'demo': 'https://api.worldoftanks'})
@patch('wargaming.meta.open', open_schema)
def get_demo_class():
    class Demo(six.with_metaclass(MetaAPI, BaseAPI)):
        def __init__(self, *args, **kwargs):
            super(Demo, self).__init__(*args, **kwargs)
            self.sub_module_name.func3 = lambda: True
    return Demo


class WargamingMetaTestCase(unittest.TestCase):
    @patch('wargaming.meta.ALLOWED_GAMES', ['demo'])
    @patch('wargaming.meta.GAME_API_ENDPOINTS', {'demo': 'https://api.worldoftanks'})
    @patch('wargaming.meta.open', open_schema)
    def setUp(self):
        self.demo = get_demo_class()('demo', 'ru', 'ru')

    def test_invalid_game(self):
        with self.assertRaises(ValidationError):
            class Demo(six.with_metaclass(MetaAPI, BaseAPI)):
                pass

    def test_invalid_region(self):
        with self.assertRaises(ValidationError):
            WoT('demo', 'ua', 'ua')

    @patch('wargaming.meta.requests.get')
    def test_call_api(self, get):
        base_url = self.demo.base_url
        self.demo.sub_module_name.func1()._fetch_data()
        get.assert_called_once_with(
            base_url + 'sub_module_name/func1/',
            params={
                'language': self.demo.language,
                'application_id': self.demo.application_id,
            },
            headers={
                'User-Agent': HTTP_USER_AGENT_HEADER,
            }
        )

        get.reset_mock()
        self.demo.sub_module_name.func2(application_id=1, language=1,
                                        fields=list(range(3)))\
            ._fetch_data()
        get.assert_called_once_with(
            base_url + 'sub_module_name/func2/',
            params={
                'language': 1,
                'application_id': 1,
                'fields': '0,1,2',
            },
            headers={
                'User-Agent': HTTP_USER_AGENT_HEADER,
            }
        )

    def test_parameters_tuple_list_join(self):
        fields = ['f1', 'f2', 'f3']
        res = self.demo.sub_module_name.func2(fields=fields)
        self.assertEqual(','.join(fields), res.params['fields'])

        fields = [1, 2, 3]
        res = self.demo.sub_module_name.func2(fields=fields)
        self.assertEqual(','.join([str(i) for i in fields]), res.params['fields'])

        fields = (1, 2, 3)
        res = self.demo.sub_module_name.func2(fields=fields)
        self.assertEqual(','.join([str(i) for i in fields]), res.params['fields'])

    def test_parameters_convert_date(self):
        date = datetime(2016, 1, 1, 13, 0, 0)
        res = self.demo.sub_module_name.func2(date=date)
        self.assertEqual(date.isoformat(), res.params['date'])

    def test_parameters_schema_function_wrong_parameter(self):
        with self.assertRaises(ValidationError):
            self.demo.sub_module_name.func1(wrong_parameter='123')

    def test_parameters_schema_function_missing_required_parameter(self):
        with self.assertRaises(ValidationError):
            self.demo.sub_module_name.func4()
        self.demo.sub_module_name.func4(clan_id='123')

    @patch('wargaming.meta.requests.get')
    def test_schema_function(self, get):
        get.return_value.json.return_value = {'status': 'ok', 'data': [{'id': '123456'}]}
        value = self.demo.sub_module_name.func1()
        self.assertIsInstance(value, WGAPI)
        ret_val = list(i for i in value)
        self.assertEqual(ret_val, [{'id': '123456'}])
        get.assert_called_once_with(self.demo.base_url + 'sub_module_name/func1/',
                                    headers={'User-Agent': settings.HTTP_USER_AGENT_HEADER},
                                    params={'application_id': 'demo', 'language': 'ru'})

    def test_custom_function(self):
        self.assertEqual(self.demo.sub_module_name.func3(), True)

    @patch('wargaming.meta.requests.get')
    def test_wgapi_list(self, get):
        data = [{'id': '123456'}]
        get.return_value.json.return_value = {'status': 'ok', 'data': data}
        res = WGAPI('http://apiurl/')
        self.assertEqual(res[0], data[0])
        self.assertEqual(list(res), data)

    @patch('wargaming.meta.requests.get')
    def test_wgapi_dict(self, get):
        data = {
            '123456': {'name': 'title'},
            123458: {'name': 'title 3'},
        }
        get.return_value.json.return_value = {'status': 'ok', 'data': data}
        res = WGAPI('http://apiurl/')
        # test conversion of numeric keys
        self.assertEqual(res[123456], data['123456'])
        self.assertEqual(res['123456'], data['123456'])
        self.assertEqual(res[123458], data[123458])
        self.assertEqual(res['123458'], data[123458])
        self.assertEqual(dict(res), data)
        self.assertTrue(all(i in res.values() for i in data.values()))

    @patch('wargaming.meta.requests.get')
    def test_wgapi_strings(self, get):
        data = [{'id': '123456'}]
        get.return_value.json.return_value = {'status': 'ok', 'data': data}
        res = WGAPI('http://apiurl/')
        self.assertEqual(str(res), str(data))
        self.assertEqual(repr(res), str(data))

        data = [{'id': '123456'}] * 20
        get.return_value.json.return_value = {'status': 'ok', 'data': data}
        res = WGAPI('http://apiurl/')
        self.assertEqual(repr(res), str(data)[0:200] + '...')

    @patch('wargaming.meta.requests.get')
    def test_wgapi_retry(self, get):
        get.return_value.json.return_value = {'status': 'error', 'error': {
            'code': 504,
            'field': None,
            'message': u'SOURCE_NOT_AVAILABLE',
            'value': None
        }}
        res = WGAPI('http://apiurl/')
        with self.assertRaises(RequestError):
            res._fetch_data()
        self.assertEqual(get.return_value.json.call_count, RETRY_COUNT)

    @patch('wargaming.meta.requests.get')
    def test_wg_unofficial(self, get):
        get.return_value.json.return_value = [{'id': '123456'}]
        wot = WoT('demo', 'ru', 'ru')
        with self.assertRaises(ValidationError):
            wot.globalmap.wg_clan_battles('')
        res = wot.globalmap.wg_clan_battles(123)
        self.assertIsInstance(res, WGAPI)


class WargamingMetaWithParserTestCase(WargamingMetaTestCase):
    @patch('wargaming.meta.ALLOWED_GAMES', ['demo'])
    @patch('wargaming.meta.GAME_API_ENDPOINTS', {'demo': 'https://api.worldoftanks'})
    @patch('wargaming.meta.open', open_schema)
    def setUp(self):
        self.demo = get_demo_class()('demo', 'ru', 'ru', enable_parser=True)

    @patch('wargaming.meta.requests.get')
    def test_field_datetime_conversion(self, get):
        get.return_value.json.return_value = {
            'status': 'ok', 'data': {'integer': '1', 'timestamp': 1}}
        res = self.demo.sub_module_name.func1()
        self.assertEqual(res.data, {'integer': 1, 'timestamp': datetime.fromtimestamp(1)})


class WargamingTestCase(unittest.TestCase):
    @staticmethod
    def test_real_schema():
        WoT('demo', 'ru', 'ru')
        WGN('demo', 'ru', 'ru')
        WoTB('demo', 'ru', 'ru')
        WoWP('demo', 'ru', 'ru')
        WoWS('demo', 'ru', 'ru')
        WoTX('demo', 'ru', 'ru')
