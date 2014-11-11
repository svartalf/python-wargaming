# -*- coding: utf-8 -*-

import unittest2 as unittest

from wargaming.games.wot import API


class WOTTestCase(unittest.TestCase):

    def setUp(self):
        self.api = API(application_id='demo')

    def test_list_of_players(self):
        response = self.api.accounts.list(search='demo', limit=5)
        self.assertEqual(5, len(response))
