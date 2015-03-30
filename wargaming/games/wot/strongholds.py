from wargaming.api import SubclassAPI, bind


class Strongholds(SubclassAPI):

    info = bind(path='stronghold/info/',
        allowed_params=('fields', 'language', 'clan_id', 'access_token'),
        doc='''Clan's stronghold

        :reference: https://wargaming.net/developers/api_reference/wot/stronghold/info/''')

    structures = bind(path='stronghold/buildings/',
        allowed_params=('fields', 'language'),
        doc='''Encyclopedia information on all structures of the Stronghold.

        :reference: https://wargaming.net/developers/api_reference/wot/stronghold/buildings/''')

    account_stats = bind('stronghold/accountstats/',
        allowed_params=('fields', 'language', 'access_token', 'account_id'),
        doc='''Player stats for the current clan's Stronghold..

        :reference: https://wargaming.net/developers/api_reference/wot/stronghold/accountstats/''')
