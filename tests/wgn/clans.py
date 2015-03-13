# -*- coding: utf-8 -*-

from tests.wgn import WGNTestCase

from wargaming.exceptions import APIError


class WGNClansTestCase(WGNTestCase):

    def setUp(self):
        super(WGNClansTestCase, self).setUp()
        self.clan_id = 1000000000

    def test_list(self):
        response = self.api.clans.list(limit=3)
        self.assertEqual(3, len(response))

    def test_info(self):
        # Empty `clan_id` parameter
        self.assertRaises(APIError, self.api.clans.info)


        response = self.api.clans.info(clan_id=self.clan_id)
        self.assertIn(str(self.clan_id), response)
        self.assertEqual(1, len(response))

    def test_membersinfo(self):
        account_id = 1000000000
        response = self.api.clans.membersinfo(account_id=account_id)

        self.assertIn(str(account_id), response)
