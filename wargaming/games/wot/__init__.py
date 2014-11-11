# -*- coding: utf-8 -*-

import six

from wargaming.api import BaseAPI, MetaAPI
from wargaming.games.wot.accounts import Accounts
from wargaming.games.wot.auth import Auth


__all__ = ('API', )


@six.add_metaclass(MetaAPI)
class API(BaseAPI):

    def __init__(self, application_id, base_url='https://api.worldoftanks.com/wot/'):
        super(API, self).__init__(application_id, base_url)

    accounts = Accounts()

    auth = Auth()
