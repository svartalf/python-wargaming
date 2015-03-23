from wargaming.api import SubclassAPI, bind


class Encyclopedia(SubclassAPI):

    vehicles = bind(path='encyclopedia/vehicles/',
        allowed_params=('fields', 'language', 'tank_id', 'nation'),
        doc='''List of vehicles

        :reference: https://wargaming.net/developers/api_reference/wotb/encyclopedia/vehicles/''')

    vehicle_profiles = bind(path='encyclopedia/vehicleprofiles/',
        allowed_params=('fields', 'language', 'tank_id', 'is_default'),
        doc='''Vehicle characteristics

        :reference: https://wargaming.net/developers/api_reference/wotb/encyclopedia/vehicleprofiles/''')

    modules = bind(path='encyclopedia/modules/',
        allowed_params=('fields', 'language', 'module_id'),
        doc='''Available modules, such as guns, engines, etc.

        :reference: https://wargaming.net/developers/api_reference/wotb/encyclopedia/modules/''')

    provisions = bind(path='encyclopedia/provisions/',
        allowed_params=('fields', 'language', 'type', 'provision_id', 'type_id'),
        doc='''Available equipment and consumables.

        :reference: https://wargaming.net/developers/api_reference/wotb/encyclopedia/provisions/''')

    info = bind(path='encyclopedia/info/',
        allowed_params=('fields', 'language'),
        doc='''Tankopedia information

        :reference: https://wargaming.net/developers/api_reference/wotb/encyclopedia/info/''')
