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
