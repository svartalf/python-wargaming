from wargaming.api import SubclassAPI, bind


class ClanRatings(SubclassAPI):

    types = bind(path='clanratings/types/',
        allowed_params=('fields', 'language'),
        doc='''Types of ratings

        :reference: http://wargaming.net/developers/api_reference/wot/clanratings/types/''')

    dates = bind(path='clanratings/dates/',
        allowed_params=('fields', 'language', 'type', 'clan_id'),
        doc='''Dates with available ratings

        :reference: http://wargaming.net/developers/api_reference/wot/clanratings/dates/''')

    clans = bind(path='clanratings/clans/',
        allowed_params=('fields', 'language', 'type', 'date', 'clan_id'),
        doc='''Clan ratings

        :reference: http://wargaming.net/developers/api_reference/wot/clanratings/clans/''')

    neighbors = bind(path='clanratings/neighbors/',
        allowed_params=('fields', 'language', 'type', 'date', 'clan_id', 'rank_field', 'limit'),
        doc='''Adjacent positions in clan rating

        :reference: http://na.wargaming.net/developers/api_reference/wot/clanratings/neighbors/''')

    top = bind(path='clanratings/top/',
        allowed_params=('fields', 'language', 'type', 'date', 'rank_field', 'limit'),
        doc='''Top clans

        :reference: http://na.wargaming.net/developers/api_reference/wot/clanratings/top/''')
