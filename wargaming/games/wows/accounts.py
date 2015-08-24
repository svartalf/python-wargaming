from wargaming.api import SubclassAPI, bind


class Accounts(SubclassAPI):
    """Players information, vehicles and achievements"""

    list = bind(path='account/list/',
        allowed_params=('fields', 'language', 'type', 'search', 'limit'),
        doc='''List of players

        :reference: https://wargaming.net/developers/api_reference/wows/account/list/''')

    info = bind(path='account/info/',
        allowed_params=('fields', 'language', 'account_id', 'access_token', 'extra'),
        doc='''Player personal data

        :reference: https://wargaming.net/developers/api_reference/wows/account/info/''')

    achievements = bind(path='account/achievements/',
        allowed_params=('fields', 'language', 'account_id'),
        doc='''Player's achievements

        :reference: https://wargaming.net/developers/api_reference/wows/account/achievements/''')
