from wargaming.exceptions import APIError, RequestError, ValidationError

import six

from wargaming.meta import MetaAPI

@six.add_metaclass(MetaAPI)
class WoT(object):
    pass


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
