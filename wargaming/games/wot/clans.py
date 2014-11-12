from wargaming.api import SubclassAPI
from wargaming.binder import bind


class Clans(SubclassAPI):

    list = bind(path='clan/list',
                allowed_params=('fields', 'language', 'search', 'limit', 'order_by', 'page_no'),
                doc='''Clans
                :reference:https://wargaming.net/developers/api_reference/wot/clan/list/''')

    info = bind(path='clan/info/',
                allowed_params=('fields', 'language', 'clan_id', 'access_token'),
                doc='''Clan details
                :reference:https://wargaming.net/developers/api_reference/wot/clan/info/''')

    top = bind(path='clan/top/',
               allowed_params=('fields', 'language', 'map_id', 'time'),
               doc='''Top clans by victory points
               :reference:https://wargaming.net/developers/api_reference/wot/clan/top/
               ''')

    provinces = bind(path='clan/provinces/',
                     allowed_params=('fields', 'language', 'map_id', 'clan_id', 'access_token'),
                     doc='''Clan's provinces
                     :reference:https://wargaming.net/developers/api_reference/wot/clan/provinces/''')

    victorypoints = bind(path='clan/victorypoints/',
                         allowed_params=('fields', 'language', 'clan_id'),
                         doc='''Clan victory points
                         :reference:https://wargaming.net/developers/api_reference/wot/clan/victorypoints/''')

    membersinfo = bind(path='clan/membersinfo/',
                       allowed_params=('fields', 'language', 'member_id'),
                       doc='''Clan member
                       :reference:https://wargaming.net/developers/api_reference/wot/clan/membersinfo/''')
