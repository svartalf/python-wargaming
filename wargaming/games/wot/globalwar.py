from wargaming.api import SubclassAPI
from wargaming.binder import bind


class GlobalWar(SubclassAPI):

    clans = bind(path='globalwar/clans',
                allowed_params=('fields', 'language', 'map_id', 'limit', 'page_no'),
                doc='''Clans
                :reference:https://wargaming.net/developers/api_reference/wot/globalwar/clans/''')

    famepoints = bind(path='globalwar/famepoints/',
                allowed_params=('fields', 'language', 'map_id', 'account_id'),
                doc='''Fame points
                :reference:https://na.wargaming.net/developers/api_reference/wot/globalwar/famepoints/''')

    maps = bind(path='globalwar/maps/',
               allowed_params=('fields', 'language'),
               doc='''Maps
               :reference:https://wargaming.net/developers/api_reference/wot/globalwar/maps/
               ''')

    provinces = bind(path='globalwar/provinces/',
                     allowed_params=('fields', 'language', 'map_id', 'province_id', 'region_id'),
                     doc='''Provinces
                     :reference:https://wargaming.net/developers/api_reference/wot/globalwar/provinces/''')

    top = bind(path='globalwar/top/',
               allowed_params=('fields', 'language', 'map_id', 'order_by'),
               doc='''Top clans
               :reference:https://wargaming.net/developers/api_reference/wot/globalwar/top/''')
