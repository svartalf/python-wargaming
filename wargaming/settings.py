from wargaming.version import get_version


HTTP_USER_AGENT_HEADER = 'python-wargaming/{0} (https://github.com/svartalf/python-wargaming)'.format(get_version())

DEFAULT_LANGUAGE = 'en'
DEFAULT_CLUSTER  = 'na'

ALLOWED_LANGUAGES = ('en', 'ru', 'pl', 'de', 'fr', 'es', 'zh-cn', 'tr', 'cs',
                     'th', 'vi', 'ko')

ALLOWED_CLUSTERS = {'eu' : 'eu', 'na' : 'com', 'asia' : 'asia', 'ru' : 'ru', 'kr' : 'kr'}
