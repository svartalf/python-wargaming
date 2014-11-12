# -*- coding: utf-8 -*-

from tests import WargamingTestCase


class WOTAuthTestCase(WargamingTestCase):

    def setUp(self):
        super(WOTAuthTestCase, self).setUp()

    def test_login(self):
        response = self.api.auth.login(redirect_uri='https://na.wargaming.net/developers/api_explorer/wot/auth/login/complete/',
                                       nofollow=True)
        self.assertIn('location', response)
