from wargaming.version import get_version

ALLOWED_GAMES = ['wot', 'wgn', 'wows', 'wotb', 'wowp']

ALLOWED_REGIONS = ['ru', 'asia', 'na', 'eu', 'kr']
DEFAULT_REGION = 'ru'

HTTP_USER_AGENT_HEADER = 'python-wargaming/%s' % get_version()
