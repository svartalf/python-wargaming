# -*- coding: utf-8 -*-

import six

from wargaming import settings
from wargaming.api import BaseAPI, MetaAPI
from .clans import Clans

__all__ = ('API', )


@six.add_metaclass(MetaAPI)
class API(BaseAPI):
    """Wargaming.NET API client"""

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
                                  base_url='https://api.worldoftanks.{0}/wgn/'.format(self.get_tld_for_cluster(cluster)))

    clans = Clans()
