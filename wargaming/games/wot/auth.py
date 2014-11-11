from wargaming.api import SubclassAPI
from wargaming.binder import bind


class Auth(SubclassAPI):

    login = bind(path='auth/login/',
        allowed_params=('fields', 'language', 'expires_at', 'redirect_uri', 'display', 'nofollow'),
        doc='''OpenID login
        https://wargaming.net/developers/api_reference/wot/auth/login/''')

    prolongate = bind(path='auth/prolongate/',
        allowed_params=('expires_at', 'access_token'),
        doc='''Access token extension
        https://wargaming.net/developers/api_reference/wot/auth/prolongate/''')

    logout = bind(path='auth/logout/',
        allowed_params=('access_token'),
        doc='''Log out
        https://wargaming.net/developers/api_reference/wot/auth/logout/''')
