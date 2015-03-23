# -*- coding: utf-8 -*-

from tests.wotb import WoTBTestCase


class WOTBTanksTestCase(WoTBTestCase):

    def setUp(self):
        super(WOTBTanksTestCase, self).setUp()
        self.account_id = 1000000000

    def test_stats(self):
        self.assertValidResponse(self.api.tanks.stats, account_id=self.account_id)

    def test_achievements(self):
        self.assertValidResponse(self.api.tanks.achievements, account_id=self.account_id)
