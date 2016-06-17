from wargaming.version import get_version

ALLOWED_GAMES = ('wot', 'wgn', 'wows', 'wotb', 'wowp')

ALLOWED_REGIONS = ('ru', 'asia', 'na', 'eu', 'kr')
REGION_API_ENDPOINTS = {
    'ru': 'https://api.worldoftanks.ru',
    'asia': 'https://api.worldoftanks.asia',
    'na': 'https://api.worldoftanks.com',
    'eu': 'https://api.worldoftanks.eu',
    'kr': 'https://api.worldoftanks.kr',
}
DEFAULT_REGION = 'ru'

ALLOWED_LANGUAGES = ('en', 'ru', 'pl', 'de', 'fr', 'es', 'zh-cn', 'tr', 'cs', 'th', 'vi', 'ko')
DEFAULT_LANGUAGE = 'en'

HTTP_USER_AGENT_HEADER = 'python-wargaming/{0} (https://github.com/svartalf/python-wargaming)'.format(get_version())

# How many times retry api call
RETRY_COUNT = 10
