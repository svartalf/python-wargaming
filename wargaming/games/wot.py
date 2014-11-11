# -*- coding: utf-8 -*-

from wargaming.api import BaseAPI
from wargaming.binder import bind


__all__ = ('API', )


class API(BaseAPI):

    def __init__(self, application_id, base_url='https://api.worldoftanks.com/wot/'):
        super(API, self).__init__(application_id, base_url)

    account_list = bind(path='account/list/',
                        allowed_params=('fields', 'language', 'type', 'search', 'limit'),
                        doc='''List of players
                        https://na.wargaming.net/developers/api_reference/wot/account/list/''')

    account_info = bind(path='account/info/',
                        allowed_params=('fields', 'language', 'account_id', 'access_token'),
                        doc='''Player personal data
                        https://na.wargaming.net/developers/api_reference/wot/account/info/''')
