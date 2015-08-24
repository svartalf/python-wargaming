# -*- coding: utf-8 -*-

from tests.wows import WoWSTestCase


class WOWSShipsTestCase(WoWSTestCase):

    def setUp(self):
        super(WOWSShipsTestCase, self).setUp()
        self.account_id = 1000000000

    def test_stats(self):
        self.assertValidResponse(self.api.ships.stats, account_id=self.account_id)
