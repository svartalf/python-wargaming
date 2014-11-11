# -*- coding: utf-8 -*-

import unittest2 as unittest

from wargaming.games.wot import API
from wargaming.exceptions import ValidationError


class APITestCase(unittest.TestCase):

    def setUp(self):
        self.api = API(application_id='demo')

    def test_invalid_language(self):
        self.assertRaises(ValidationError, self.api.accounts.list,
                          search='test', language='tlh')  # Klingon lang ;)
