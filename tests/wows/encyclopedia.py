# -*- coding: utf-8 -*-

from tests.wows import WoWSTestCase


class WOWSEncyclopediaTestCase(WoWSTestCase):

    def setUp(self):
        super(WOWSEncyclopediaTestCase, self).setUp()
        self.ship_id = 1
        self.nation = 'ussr'

    def test_warships(self):
        self.assertValidResponse(self.api.encyclopedia.warships)

    def test_achievements(self):
        self.assertValidResponse(self.api.encyclopedia.achievements)

    def test_info(self):
        self.assertValidResponse(self.api.encyclopedia.info)

    def test_modules(self):
        self.assertValidResponse(self.api.encyclopedia.modules)

    def test_upgrades(self):
        self.assertValidResponse(self.api.encyclopedia.upgrades)
