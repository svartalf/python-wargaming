# -*- coding: utf-8 -*-

from tests.wot import WotTestCase


class WOTStrongholdsTestCase(WotTestCase):

    def setUp(self):
        super(WOTStrongholdsTestCase, self).setUp()
        self.clan_id = 1000000001
        self.account_id = 1000000000
        self.province_id = 'US_01'

    def test_info(self):
        self.assertValidResponse(self.api.strongholds.info, clan_id=self.clan_id)

    def test_structures(self):
        self.assertValidResponse(self.api.strongholds.structures)

    def test_account_stats(self):
        self.assertValidResponse(self.api.strongholds.account_stats, account_id=self.account_id)
