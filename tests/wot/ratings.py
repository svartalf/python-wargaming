# -*- coding: utf-8 -*-

from tests import WargamingTestCase


class WOTRatingsTestCase(WargamingTestCase):

    def setUp(self):
        super(WOTRatingsTestCase, self).setUp()
        self.account_id = 1000000000
        self.rank_field = 'frags_count'

    def test_types(self):
        self.assertValidResponse(self.api.ratings.types)

    def test_dates(self):
        self.assertValidResponse(self.api.ratings.dates, type='all')

    def test_accounts(self):
        self.assertValidResponse(self.api.ratings.accounts, type='all')

    def test_neighbors(self):
        self.assertValidResponse(self.api.ratings.neighbors, type='all',
                                 account_id=self.account_id, rank_field=self.rank_field)

    def test_top(self):
        self.assertValidResponse(self.api.ratings.top, type='all',
                                 rank_field=self.rank_field)
