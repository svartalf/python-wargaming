# -*- coding: utf-8 -*-

from tests import WargamingTestCase


class WOTClanRatingsTestCase(WargamingTestCase):

    def setUp(self):
        super(WOTClanRatingsTestCase, self).setUp()
        self.clan_id = 1000000001
        self.rating_period = 'all'
        self.rank_field = 'efficiency'

    def test_types(self):
        self.assertValidResponse(self.api.clan_ratings.types)

    def test_dates(self):
        self.assertValidResponse(self.api.clan_ratings.dates, type=self.rating_period, clan_id=self.clan_id)

    def test_clans(self):
        self.assertValidResponse(self.api.clan_ratings.clans, type=self.rating_period, clan_id=self.clan_id)

    def test_neighbors(self):
        self.assertValidResponse(self.api.clan_ratings.neighbors, type=self.rating_period, clan_id=self.clan_id,
                                 rank_field=self.rank_field)

    def test_top(self):
        self.assertValidResponse(self.api.clan_ratings.top, type=self.rating_period, rank_field=self.rank_field)
