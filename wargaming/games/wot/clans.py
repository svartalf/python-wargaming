from wargaming.api import SubclassAPI, bind


class Clans(SubclassAPI):

    provinces = bind(path='clan/provinces/',
        allowed_params=('fields', 'language', 'map_id', 'clan_id', 'access_token'),
        doc='''Clan's provinces

        :reference: https://wargaming.net/developers/api_reference/wot/clan/provinces/''')
