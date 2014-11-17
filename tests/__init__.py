# -*- coding: utf-8 -*-

import unittest2 as unittest

from wargaming.games.wot import API
from wargaming.exceptions import APIError


class WargamingTestCase(unittest.TestCase):

    def setUp(self):
        self.api = API(application_id='demo')

    def assertValidResponse(self, method, **kwargs):
        try:
            response = method(**kwargs)
        except APIError as e:
            self.fail('Method {0} returns error response: {1}'.format(method, e.message))
