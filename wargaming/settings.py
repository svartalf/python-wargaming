from wargaming.version import get_version

ALLOWED_GAMES = ('wot', 'wgn', 'wows', 'wotb', 'wotx', 'wowp')

# WG classes xbox and ps4 as 'regions' hence they are incuded here
ALLOWED_REGIONS = ('ru', 'asia', 'na', 'eu', 'kr', 'xbox', 'ps4')
REGION_API_EXT = {
    'ru': 'ru',
    'asia': 'asia',
    'na': 'com',
    'eu': 'eu',
    'kr': 'kr',
    'ps4': 'com',
    'xbox': 'com',
}
GAME_API_ENDPOINTS = {
    'wgn': 'https://api.worldoftanks',
    'wot': 'https://api.worldoftanks',
    'wotb': 'https://api.wotblitz',
    'wotx': 'https://api-xbox-console.worldoftanks',
    'wotp': 'https://api-ps4-console.worldoftanks',
    'wowp': 'https://api.worldofwarplanes',
    'wows': 'https://api.worldofwarships',
    }

DEFAULT_REGION = 'ru'

ALLOWED_LANGUAGES = ('en', 'ru', 'pl', 'de', 'fr', 'es', 'zh-cn', 'tr', 'cs', 'th', 'vi', 'ko')
DEFAULT_LANGUAGE = 'en'

HTTP_USER_AGENT_HEADER = 'python-wargaming/{0} (https://github.com/svartalf/python-wargaming)'.format(get_version())

# How many times retry api call
RETRY_COUNT = 10
