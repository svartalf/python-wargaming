# -*- coding: utf-8 -*-

from tests import WargamingTestCase


class WOTEncyclopediaTestCase(WargamingTestCase):

    def setUp(self):
        super(WOTEncyclopediaTestCase, self).setUp()
        self.tank_id = 1
        self.nation = 'ussr'

    def test_tanks(self):
        self.assertValidResponse(self.api.encyclopedia.tanks)

    def test_tank_info(self):
        self.assertValidResponse(self.api.encyclopedia.tank_info,
                                 tank_id=self.tank_id)

    def test_tank_engines(self):
        self.assertValidResponse(self.api.encyclopedia.tank_engines,
                                 nation=self.nation)

    def test_tank_turrets(self):
        self.assertValidResponse(self.api.encyclopedia.tank_turrets,
                                 nation=self.nation)

    def test_tank_radios(self):
        self.assertValidResponse(self.api.encyclopedia.tank_radios,
                                 nation=self.nation)

    def test_tank_suspensions(self):
        self.assertValidResponse(self.api.encyclopedia.tank_suspensions,
                                 nation=self.nation)

    def test_tank_guns(self):
        self.assertValidResponse(self.api.encyclopedia.tank_guns,
                                 tank_id=self.tank_id)

    def test_achievements(self):
        self.assertValidResponse(self.api.encyclopedia.achievements)

    def test_info(self):
        self.assertValidResponse(self.api.encyclopedia.info)

    def test_arenas(self):
        self.assertValidResponse(self.api.encyclopedia.arenas)
