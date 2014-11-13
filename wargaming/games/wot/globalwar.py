from wargaming.api import SubclassAPI
from wargaming.binder import bind


class GlobalWar(SubclassAPI):

    clans = bind(path='globalwar/clans/',
        allowed_params=('fields', 'language', 'map_id', 'limit', 'page_no'),
        doc='''Clans
        :reference:https://wargaming.net/developers/api_reference/wot/globalwar/clans/''')

    fame_points = bind(path='globalwar/famepoints/',
        allowed_params=('fields', 'language', 'map_id', 'account_id'),
        doc='''Fame points
        :reference:https://na.wargaming.net/developers/api_reference/wot/globalwar/famepoints/''')

    maps = bind(path='globalwar/maps/',
        allowed_params=('fields', 'language'),
        doc='''Maps
        :reference:https://wargaming.net/developers/api_reference/wot/globalwar/maps/''')

    provinces = bind(path='globalwar/provinces/',
        allowed_params=('fields', 'language', 'map_id', 'province_id', 'region_id'),
        doc='''Provinces
        :reference:https://wargaming.net/developers/api_reference/wot/globalwar/provinces/''')

    top = bind(path='globalwar/top/',
        allowed_params=('fields', 'language', 'map_id', 'order_by'),
        doc='''Top clans
        :reference:https://wargaming.net/developers/api_reference/wot/globalwar/top/''')

    tournaments = bind(path='globalwar/tournaments/',
        allowed_params=('fields', 'language', 'map_id', 'province_id'),
        doc='''Tournaments
        :reference:https://wargaming.net/developers/api_reference/wot/globalwar/tournaments/''')

    fame_points_history = bind(path='globalwar/famepointshistory/',
        allowed_params=('fields', 'language', 'map_id', 'since', 'until', 'page_no', 'limit', 'access_token'),
        doc='''Player's fame points log
        https://wargaming.net/developers/api_reference/wot/globalwar/famepointshistory/''')

    alley_of_fame = bind(path='globalwar/alleyoffame/',
        allowed_params=('fields', 'language', 'map_id', 'limit', 'page_no'),
        doc='''Alley of fame
        :reference:https://wargaming.net/developers/api_reference/wot/globalwar/alleyoffame/''')

    battles = bind(path='globalwar/battles/',
        allowed_params=('fields', 'language', 'map_id', 'clan_id', 'access_token'),
        doc='''Clan's battles
        :reference:https://wargaming.net/developers/api_reference/wot/globalwar/battles/''')

    victory_points_history = bind(path='globalwar/victorypointshistory/',
        allowed_params=('fields', 'language', 'map_id', 'clan_id', 'since', 'until', 'offset', 'limit'),
        doc='''Clan victory points log
        :rerefence:https://wargaming.net/developers/api_reference/wot/globalwar/victorypointshistory/''')
