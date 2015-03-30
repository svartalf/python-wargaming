# -*- coding: utf-8 -*-

from tests.wot import WotTestCase


class WOTClansTestCase(WotTestCase):

    def setUp(self):
        super(WOTClansTestCase, self).setUp()
        self.clan_id = 1000000000

    def test_provinces(self):
        # Have no ideas what that method should returns, so just verifying
        #   that request was made
        # TODO: check for proper response
        self.api.clans.provinces(clan_id=self.clan_id)
