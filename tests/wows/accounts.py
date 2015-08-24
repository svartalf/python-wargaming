# -*- coding: utf-8 -*-

from tests.wows import WoWSTestCase


class WOWSAccountsTestCase(WoWSTestCase):

    def setUp(self):
        super(WOWSAccountsTestCase, self).setUp()

        self.ids = [1000000001, 1000000002]

    def test_list(self):
        response = self.api.accounts.list(search='demo', limit=5)
        self.assertEqual(5, len(response))

    def test_info(self):
        response = self.api.accounts.info(account_id=self.ids)

        self.assertEqual(len(self.ids), len(response))

        for id_ in self.ids:
            self.assertIn(str(id_), response)

    def test_achievements(self):
        response = self.api.accounts.achievements(account_id=self.ids)

        self.assertEqual(len(self.ids), len(response))

        for id_ in self.ids:
            self.assertIn(str(id_), response)
