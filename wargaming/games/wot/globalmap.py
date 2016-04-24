from wargaming.api import SubclassAPI, bind


class GlobalMap(SubclassAPI):
    fronts = bind(path='globalmap/fronts/',
        allowed_params=('fields', 'language', 'limit', 'page_no', 'front_id'),
        doc='''Fronts

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/fronts/''')

    provinces = bind(path='globalmap/provinces/',
        allowed_params=('fields', 'language', 'limit', 'page_no', 'front_id', 'prime_hour',
                        'landing_type', 'arena_id', 'daily_revenue_lte', 'daily_revenue_gte',
                        'order_by', 'province_id'),
        doc='''Provinces

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/provinces/''')

    claninfo = bind(path='globalmap/claninfo/',
        allowed_params=('fields', 'access_token', 'clan_id'),
        doc='''Clan info

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/claninfo/''')

    clanprovinces = bind(path='globalmap/clanprovinces/',
        allowed_params=('fields', 'access_token', 'language', 'clan_id'),
        doc='''Clan provinces

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/clanprovinces/''')

    clanbattles = bind(path='globalmap/clanbattles/',
        allowed_params=('fields', 'language', 'limit', 'page_no', 'clan_id'),
        doc='''Clan's battles

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/clanbattles/''')

    seasons = bind(path='globalmap/seasons/',
        allowed_params=('fields', 'language', 'page_no', 'season_id', 'limit', 'status'),
        doc='''Seasons

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/seasons/''')

    seasonclaninfo = bind(path='globalmap/seasonclaninfo/',
        allowed_params=('fields', 'season_id', 'vehicle_level', 'clan_id'),
        doc='''Season clan info

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/seasonclaninfo/''')

    seasonaccountinfo = bind(path='globalmap/seasonaccountinfo/',
        allowed_params=('fields', 'season_id', 'vehicle_level', 'account_id'),
        doc='''Season account info

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/seasonaccountinfo/''')

    seasonrating = bind(path='globalmap/seasonrating/',
        allowed_params=('fields', 'page_no', 'limit', 'season_id', 'vehicle_level'),
        doc='''Season rating

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/seasonrating/''')

    seasonratingneighbors = bind(path='globalmap/seasonratingneighbors/',
        allowed_params=('fields', 'season_id', 'vehicle_level', 'clan_id', 'limit'),
        doc='''Season rating neighbors

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/seasonratingneighbors/''')

    events = bind(path='globalmap/events/',
        allowed_params=('fields', 'language', 'page_no', 'event_id', 'limit', 'status'),
        doc='''Events

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/events/''')

    eventclaninfo = bind(path='globalmap/eventclaninfo/',
        allowed_params=('fields', 'event_id', 'front_id', 'clan_id'),
        doc='''Event clan info

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/eventclaninfo/''')

    eventclantasks = bind(path='globalmap/eventclantasks/',
        allowed_params=('fields', 'language', 'page_no', 'limit', 'clan_id', 'event_id'),
        doc='''Event clan tasks

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/eventclantasks/''')

    eventaccountinfo = bind(path='globalmap/eventaccountinfo/',
        allowed_params=('fields', 'event_id', 'front_id', 'account_id'),
        doc='''Event account info

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/eventaccountinfo/''')

    eventaccountratings = bind(path='globalmap/eventaccountratings/',
        allowed_params=('fields', 'page_no', 'event_id', 'front_id', 'limit', 'in_rating'),
        doc='''Event account ratings

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/eventaccountratings/''')

    eventaccountratingneighbors = bind(path='globalmap/eventaccountratingneighbors/',
        allowed_params=('fields', 'page_no', 'event_id', 'front_id', 'account_id', 'limit', 'neighbours_count'),
        doc='''Event account rating neighbors

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/eventaccountratingneighbors/''')

    eventrating = bind(path='globalmap/eventrating/',
        allowed_params=('fields', 'page_no', 'limit', 'event_id', 'front_id'),
        doc='''Event rating

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/eventrating/''')

    eventratingneighbors = bind(path='globalmap/eventratingneighbors/',
        allowed_params=('fields', 'event_id', 'front_id', 'clan_id', 'limit'),
        doc='''Event rating neighbors

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/eventratingneighbors/''')

    info = bind(path='globalmap/info/',
        allowed_params=('fields'),
        doc='''Info

        :reference: https://wargaming.net/developers/api_reference/wot/globalmap/info/''')
