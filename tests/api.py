# -*- coding: utf-8 -*-

import unittest2 as unittest

from wargaming import settings
from wargaming.games.wot import API
from wargaming.exceptions import ValidationError


class APITestCase(unittest.TestCase):

    def setUp(self):
        self.api = API(application_id='demo')

    def test_default_language(self):
        self.assertEqual(self.api.language, settings.DEFAULT_LANGUAGE)

        api_ru = API(application_id='demo', language='ru')
        self.assertEqual(api_ru.language, 'ru')

    def test_invalid_language(self):
        self.assertRaises(ValidationError, self.api.accounts.list,
                          search='test', language='tlh')  # Klingon lang ;)

    def test_default_cluster(self):
        self.assertEqual(self.api.url_netloc, 'api.worldoftanks.' + settings.ALLOWED_CLUSTERS[settings.DEFAULT_CLUSTER])

        api_ru = API(application_id='demo', cluster='ru')
        self.assertEqual(api_ru.url_netloc, 'api.worldoftanks.ru')

    def test_invalid_cluster(self):
        self.assertRaises(ValidationError, API, application_id='demo', cluster='vn')
