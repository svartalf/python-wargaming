from wargaming.version import get_version  # noqa

import six

from wargaming.meta import BaseAPI, MetaAPI, WGAPI
from wargaming.settings import DEFAULT_REGION
from wargaming.exceptions import ValidationError


@six.add_metaclass(MetaAPI)
class WoT(BaseAPI):
    def __init__(self, application_id, language, region=DEFAULT_REGION, enable_parser=False):
        super(WoT, self).__init__(application_id, language, region, enable_parser)

        def wg_clan_battles(clan_id):
            """Unofficial API call to list planned and current battles"""
            if not clan_id:
                raise ValidationError("Clan id can't be blank")

            return WGAPI("https://%s.wargaming.net/globalmap/game_api/clan/%s/battles"
                         % (region, clan_id))

        self.globalmap.wg_clan_battles = wg_clan_battles


@six.add_metaclass(MetaAPI)
class WGN(BaseAPI):
    pass


@six.add_metaclass(MetaAPI)
class WoTB(BaseAPI):
    pass


@six.add_metaclass(MetaAPI)
class WoTX(BaseAPI):
    pass


@six.add_metaclass(MetaAPI)
class WoWS(BaseAPI):
    pass


@six.add_metaclass(MetaAPI)
class WoWP(BaseAPI):
    pass
