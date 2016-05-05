import unittest

from mock import patch, mock_open
import mock
from wargaming import WoT, WGN, WoTB, WoWP, WoWS, settings
from wargaming.meta import MetaAPI, BaseAPI, WGAPI
from wargaming.settings import RETRY_COUNT
import six
import json
from wargaming.exceptions import ValidationError, RequestError


class WargamingMetaTestCase(unittest.TestCase):
    open_schema = mock_open(read_data=json.dumps(
        {'sub_module_name': {
            'func1': {
                '__doc__': 'doc example for func1',
                'application_id': {
                    'doc': 'doc for application_id',
                    'required': False,
                    'type': 'string',
                }
            }, 'func2': {
                '__doc__': 'doc example for func2',
                'application_id': {
                    'doc': 'doc for application_id',
                    'required': False,
                    'type': 'string',
                }
            }
        }}
    ))

    @patch('wargaming.meta.ALLOWED_GAMES', ['demo'])
    @patch('wargaming.meta.open', open_schema)
    def setUp(self):

        class Demo(six.with_metaclass(MetaAPI, BaseAPI)):
            def __init__(self, application_id, language, region):
                super(Demo, self).__init__(application_id, language, region)
                self.sub_module_name.func3 = lambda: True

        self.demo = Demo('demo', 'ru', 'ru')

    def test_schema_function_wrong_parameter(self):
        with self.assertRaises(ValidationError):
            self.demo.sub_module_name.func1(wrong_parameter='123')

    @patch('wargaming.meta.requests.get')
    def test_schema_function(self, get):
        get.return_value = mock.Mock()
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


class WargamingTestCase(unittest.TestCase):
    def test_real_schema(self):
        WoT('demo', 'ru', 'ru')
        WGN('demo', 'ru', 'ru')
        WoTB('demo', 'ru', 'ru')
        WoWP('demo', 'ru', 'ru')
        WoWS('demo', 'ru', 'ru')
