# -*- coding: utf-8 -*-

from tests import WargamingTestCase

from wargaming.exceptions import APIError


class WOTClansTestCase(WargamingTestCase):

    def setUp(self):
        super(WOTClansTestCase, self).setUp()
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

    def test_top(self):
        # Have no ideas what that method should returns, so just verifying
        #   that request was made
        # TODO: check for proper response
        self.api.clans.top(clan_id=self.clan_id)

    def test_provinces(self):
        # Have no ideas what that method should returns, so just verifying
        #   that request was made
        # TODO: check for proper response
        self.api.clans.provinces(clan_id=self.clan_id)

    def test_victorypoints(self):
        # Have no ideas what that method should returns, so just verifying
        #   that request was made
        # TODO: check for proper response
        self.api.clans.victorypoints(clan_id=self.clan_id)

    def test_membersinfo(self):
        member_id = 1000000000
        response = self.api.clans.membersinfo(member_id=member_id)

        self.assertIn(str(member_id), response)
