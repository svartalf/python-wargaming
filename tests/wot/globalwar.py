# -*- coding: utf-8 -*-

from tests import WargamingTestCase

from wargaming.exceptions import APIError


class WOTGlobalWarTestCase(WargamingTestCase):

    def setUp(self):
        super(WOTGlobalWarTestCase, self).setUp()
        self.map_id = 'globalmap'
        self.clan_id = 1000000001
        self.account_id = 1000000000
        self.province_id = 'US_01'

    def test_clans(self):
        response = self.api.globalwar.clans(map_id=self.map_id)
        self.assertGreater(len(response), 0)

    def test_fame_points(self):
        response = self.api.globalwar.fame_points(map_id=self.map_id,
                                                  account_id=self.account_id)
        self.assertIn(str(self.account_id), response)

    def test_maps(self):
        response = self.api.globalwar.maps()
        self.assertGreater(len(response), 0)

    def test_provinces(self):
        response = self.api.globalwar.provinces(map_id=self.map_id)
        self.assertGreater(len(response), 0)

    def test_top(self):
        self.api.globalwar.top(map_id=self.map_id, account_id=self.account_id,
                               order_by='wins_count')

    def test_tournaments(self):
        self.assertValidResponse(self.api.globalwar.tournaments,
                                 map_id=self.map_id, province_id=self.province_id)

    def test_fame_points_history(self):
        # Just skipping since we need a valid access token,
        #   which is unavailable this time
        pass

    def test_alley_of_fame(self):
        self.api.globalwar.alley_of_fame(map_id=self.map_id)

    def test_battles(self):
        self.api.globalwar.battles(map_id=self.map_id, clan_id=self.clan_id)
