# -*- coding: utf-8 -*-

from tests.wotb import WoTBTestCase


class WOTBEncyclopediaTestCase(WoTBTestCase):

    def setUp(self):
        super(WOTBEncyclopediaTestCase, self).setUp()
        self.tank_id = 1
        self.nation = 'ussr'

    def test_vehicles(self):
        self.assertValidResponse(self.api.encyclopedia.vehicles)

    def test_vehicle_profiles(self):
        self.assertValidResponse(self.api.encyclopedia.vehicle_profiles,
                                 tank_id=self.tank_id)

    def test_modules(self):
        self.assertValidResponse(self.api.encyclopedia.modules)

    def test_provisions(self):
        self.assertValidResponse(self.api.encyclopedia.provisions)

    def test_info(self):
        self.assertValidResponse(self.api.encyclopedia.info)
