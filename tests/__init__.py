# -*- coding: utf-8 -*-

import unittest2 as unittest

from wargaming.games.wot import API


class WargamingTestCase(unittest.TestCase):

    def setUp(self):
        self.api = API(application_id='demo')
