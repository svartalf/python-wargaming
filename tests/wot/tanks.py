# -*- coding: utf-8 -*-

from tests import WargamingTestCase


class WOTTanksTestCase(WargamingTestCase):

    def setUp(self):
        super(WOTTanksTestCase, self).setUp()
        self.account_id = 1000000000

    def test_stats(self):
        self.assertValidResponse(self.api.tanks.stats, account_id=self.account_id)

    def test_achievements(self):
        self.assertValidResponse(self.api.tanks.achievements, account_id=self.account_id)
