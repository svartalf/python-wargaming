# -*- coding: utf-8 -*-

from tests import WargamingTestCase

from wargaming.exceptions import APIError


class WOTGlobalWarTestCase(WargamingTestCase):

    def setUp(self):
        super(WOTGlobalWarTestCase, self).setUp()
        self.map_id = 'globalmap'
        self.account_id = 1000000000

    def test_clans(self):
        response = self.api.globalwar.clans(map_id=self.map_id)
        self.assertGreater(0, len(response))

    def test_famepoints(self):
        self.assertRaises(APIError, self.api.globalwar.famepoints)

        self.assertRaises(APIError, self.api.globalwar.famepoints,
                          map_id=self.map_id)

        self.assertRaises(APIError, self.api.globalwar.famepoints,
                          account_id=self.account_id)

        response = self.api.globalwar.famepoints(map_id=self.map_id,
                                                 account_id=self.account_id)
        self.assertIn(str(self.account_id), response)

    def test_maps(self):
        response = self.api.globalwar.maps()
        self.assertGreater(0, len(response))

    def test_provinces(self):
        self.assertRaises(APIError, self.api.globalwar.provinces)

        response = self.api.globalwar.provinces(map_id=self.map_id)
        self.assertGreater(0, len(response))

    def test_top(self):
        func = self.api.globalwar.top

        self.assertRaises(APIError, func)
        self.assertRaises(APIError, func, map_id=self.map_id)
        self.assertRaises(APIError, func, account_id=self.account_id)
        response = func(map_id=self.map_id, account_id=self.account_id)
