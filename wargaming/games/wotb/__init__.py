# -*- coding: utf-8 -*-

import six

from wargaming import settings
from wargaming.api import BaseAPI, MetaAPI
from wargaming.games.wotb.accounts import Accounts
from wargaming.games.wotb.encyclopedia import Encyclopedia
from wargaming.games.wotb.tanks import Tanks

__all__ = ('API', )


@six.add_metaclass(MetaAPI)
class API(BaseAPI):
    """World of Tanks Blitz API client"""

    def __init__(self, application_id, language=settings.DEFAULT_LANGUAGE, cluster=settings.DEFAULT_CLUSTER):
        """
        :param application_id: Your application ID from the https://wargaming.net/developers/applications/
        :type application_id: str
        :param language: Language for the requests (defaults to English)
        :type language: str
        :param cluster: id of the cluster to access
        :type cluster: str
        """

        super(API, self).__init__(application_id, language,
                                  base_url='https://api.wotblitz.{0}/wotb/'.format(self.get_tld_for_cluster(cluster)))

    accounts = Accounts()

    encyclopedia = Encyclopedia()

    tanks = Tanks()
