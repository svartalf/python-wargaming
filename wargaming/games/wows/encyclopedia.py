from wargaming.api import SubclassAPI, bind


class Encyclopedia(SubclassAPI):

    warships = bind(path='encyclopedia/ships/',
        allowed_params=('fields', 'language', 'ship_id', 'nation', 'type'),
        doc='''List of ships.

        :reference: https://wargaming.net/developers/api_reference/wows/encyclopedia/ships/''')

    achievements = bind(path='encyclopedia/achievements/',
        allowed_params=('fields', 'language'),
        doc='''Achievements.

        :reference: https://wargaming.net/developers/api_reference/wows/encyclopedia/achievements/''')

    info = bind(path='encyclopedia/info/',
        allowed_params=('fields', 'language'),
        doc='''Tankopedia information.

        :reference: https://wargaming.net/developers/api_reference/wows/encyclopedia/info/''')

    modules = bind(path='encyclopedia/modules/',
        allowed_params=('fields', 'language', 'module_id', 'type'),
        doc='''Available modules that can be installed on ships.

        :reference: https://wargaming.net/developers/api_reference/wows/encyclopedia/modules/''')

    upgrades = bind(path='encyclopedia/upgrades/',
        allowed_params=('fields', 'language', 'upgrade_id'),
        doc='''Available ship upgrades.

        :reference: https://wargaming.net/developers/api_reference/wows/encyclopedia/upgrades/''')
