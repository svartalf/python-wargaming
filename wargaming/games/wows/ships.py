from wargaming.api import SubclassAPI, bind


class Ships(SubclassAPI):

    stats = bind(path='ships/stats/',
        allowed_params=('fields', 'language', 'access_token', 'extra', 'account_id', 'ship_id', 'in_garage'),
        doc='''Statistics of player's ships.

        :reference: https://wargaming.net/developers/api_reference/wows/ships/stats/''')
