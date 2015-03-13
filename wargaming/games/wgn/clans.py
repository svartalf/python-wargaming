from wargaming.api import SubclassAPI, bind


class Clans(SubclassAPI):

    list = bind(path='clans/list/',
        allowed_params=('fields', 'language', 'search', 'limit', 'order_by', 'page_no'),
        doc='''Clans

        :reference: https://wargaming.net/developers/api_reference/wgn/clans/list/''')

    info = bind(path='clans/info/',
        allowed_params=('fields', 'language', 'clan_id', 'access_token'),
        doc='''Clan details

        :reference: https://wargaming.net/developers/api_reference/wgn/clans/info/''')

    membersinfo = bind(path='clans/membersinfo/',
        allowed_params=('fields', 'language', 'account_id'),
        doc='''Clan member

        :reference: https://wargaming.net/developers/api_reference/wgn/clans/membersinfo/''')
