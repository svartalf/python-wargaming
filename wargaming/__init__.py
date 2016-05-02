from wargaming.exceptions import APIError, RequestError, ValidationError
from wargaming.version import get_version

import six

from wargaming.meta import MetaAPI, WGAPI
from wargaming.settings import DEFAULT_REGION


@six.add_metaclass(MetaAPI)
class WoT(object):
    def __init__(self, region=DEFAULT_REGION, *args, **kwargs):
        super(WoT, self).__init__(region=region, *args, **kwargs)

        def wg_clan_battles(clan_id):
            """Unofficial API call to list planned and current battles"""
            return WGAPI("https://%s.wargaming.net/globalmap/game_api/clan/%s/battles"
                         % (region, clan_id))

        self.globalmap.wg_clan_battles = wg_clan_battles


@six.add_metaclass(MetaAPI)
class WGN(object):
    pass


@six.add_metaclass(MetaAPI)
class WoTB(object):
    pass


@six.add_metaclass(MetaAPI)
class WoWS(object):
    pass


@six.add_metaclass(MetaAPI)
class WoWP(object):
    pass
