from wargaming.api import SubclassAPI
from wargaming.binder import bind


class Accounts(SubclassAPI):
    """Players information, vehicles and achievements"""

    list = bind(path='account/list/',
        allowed_params=('fields', 'language', 'type', 'search', 'limit'),
        doc='''List of players
        :reference: https://wargaming.net/developers/api_reference/wot/account/list/'''

    info = bind(path='account/info/',
        allowed_params=('fields', 'language', 'account_id', 'access_token'),
        doc='''Player personal data
        :reference:https://wargaming.net/developers/api_reference/wot/account/info/''')

    tanks = bind(path='account/tanks/',
        allowed_params=('fields', 'language', 'account_id', 'access_token', 'tank_id'),
        doc='''Player's vehicles
        :reference:https://wargaming.net/developers/api_reference/wot/account/tanks/''')

    achievements = bind(path='account/achievements/',
        allowed_params=('fields', 'language', 'account_id'),
        doc='''Player's achievements
        :reference:https://wargaming.net/developers/api_reference/wot/account/achievements/''')
