from wargaming.api import SubclassAPI, bind


class Encyclopedia(SubclassAPI):

    tanks = bind(path='encyclopedia/tanks/',
        allowed_params=('fields', 'language'),
        doc='''List of vehicles

        :reference: https://wargaming.net/developers/api_reference/wot/encyclopedia/tanks/''')

    tank_info = bind(path='encyclopedia/tankinfo/',
        allowed_params=('fields', 'language', 'tank_id'),
        doc='''Vehicle details

        :reference: https://wargaming.net/developers/api_reference/wot/encyclopedia/tankinfo/''')

    tank_engines = bind(path='encyclopedia/tankengines/',
        allowed_params=('fields', 'language', 'module_id', 'nation'),
        doc='''Engines

        :reference: https://wargaming.net/developers/api_reference/wot/encyclopedia/tankengines/''')

    tank_turrets = bind(path='encyclopedia/tankturrets/',
        allowed_params=('fields', 'language', 'module_id', 'nation'),
        doc='''Turrets

        :reference: https://wargaming.net/developers/api_reference/wot/encyclopedia/tankturrets/''')

    tank_radios = bind(path='encyclopedia/tankradios/',
        allowed_params=('fields', 'language', 'module_id', 'nation'),
        doc='''Radios

        :reference: https://wargaming.net/developers/api_reference/wot/encyclopedia/tankradios/''')

    tank_suspensions = bind(path='encyclopedia/tankchassis/',
        allowed_params=('fields', 'language', 'module_id', 'nation'),
        doc='''Suspensions

        :reference: https://wargaming.net/developers/api_reference/wot/encyclopedia/tankchassis/''')

    tank_guns = bind(path='encyclopedia/tankguns/',
        allowed_params=('fields', 'language', 'module_id', 'nation', 'turret_id', 'tank_id'),
        doc='''

        :reference: https://wargaming.net/developers/api_reference/wot/encyclopedia/tankguns/''')

    achievements = bind(path='encyclopedia/achievements/',
        allowed_params=('fields', 'language'),
        doc='''Achievements

        :reference: https://wargaming.net/developers/api_reference/wot/encyclopedia/achievements/''')

    info = bind(path='encyclopedia/info/',
        allowed_params=('fields', 'language'),
        doc='''Tankopedia information

        :reference: https://wargaming.net/developers/api_reference/wot/encyclopedia/info/''')

    arenas = bind(path='encyclopedia/arenas/',
        allowed_params=('fields', 'language'),
        doc='''Maps details

        :reference: https://na.wargaming.net/developers/api_reference/wot/encyclopedia/arenas/''')

    vehicles = bind(path='encyclopedia/vehicles/',
        allowed_params=('fields', 'tank_id', 'nation', 'tier'),
        doc='''Vehicles

        :reference: https://wargaming.net/developers/api_reference/wot/encyclopedia/vehicles/''')

    vehicle_profile = bind(path='encyclopedia/vehicleprofile/',
        allowed_params=('fields', 'tank_id', 'engine_id', 'gun_id', 'suspension_id', 'turret_id', 'radio_id'),
        doc='''Vehicle characteristics

        :reference: https://wargaming.net/developers/api_reference/wot/encyclopedia/vehicleprofile/''')
