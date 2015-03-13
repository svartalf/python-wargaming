from wargaming.games.wot import API as WoT
from wargaming.games.wgn import API as WGN
from wargaming.exceptions import APIError, RequestError, ValidationError
from wargaming.version import get_version
from . import settings

__version__ = get_version()
