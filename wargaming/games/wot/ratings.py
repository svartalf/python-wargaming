from wargaming.api import SubclassAPI, bind


class Ratings(SubclassAPI):

    types = bind(path='ratings/types/',
        allowed_params=('language', 'fields'),
        doc='''Types of ratings

        :reference: https://wargaming.net/developers/api_reference/wot/ratings/types/''')

    dates = bind(path='ratings/dates/',
        allowed_params=('language', 'fields', 'type', 'account_id'),
        doc='''Dates with available ratings

        :reference: https://wargaming.net/developers/api_reference/wot/ratings/dates/''')

    accounts = bind(path='ratings/accounts/',
        allowed_params=('language', 'fields', 'type', 'date', 'account_id'),
        doc='''Player ratings

        :reference: https://wargaming.net/developers/api_reference/wot/ratings/accounts/''')

    neighbors = bind(path='ratings/neighbors/',
        allowed_params=('language', 'fields', 'type', 'date', 'account_id', 'rank_field', 'limit'),
        doc='''Adjacent positions in rating

        :reference: https://na.wargaming.net/developers/api_reference/wot/ratings/neighbors/''')

    top = bind(path='ratings/top/',
        allowed_params=('language', 'fields', 'type', 'date', 'account_id', 'rank_field', 'limit'),
        doc='''Top players

        :reference: https://na.wargaming.net/developers/api_reference/wot/ratings/top/''')
