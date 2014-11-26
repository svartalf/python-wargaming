from wargaming.api import SubclassAPI, bind


class Tanks(SubclassAPI):

    stats = bind(path='tanks/stats/',
        allowed_params=('language', 'fields', 'access_token', 'account_id', 'tank_id', 'in_garage'),
        doc='''Vehicle statistics

        :reference: http://wargaming.net/developers/api_reference/wot/tanks/stats/''')

    achievements = bind(path='tanks/achievements/',
        allowed_params=('language', 'fields', 'access_token', 'account_id', 'tank_id', 'in_garage'),
        doc='''Vehicle achievements

        :reference: http://wargaming.net/developers/api_reference/wot/tanks/achievements/''')
