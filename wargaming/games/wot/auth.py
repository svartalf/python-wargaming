from wargaming.api import SubclassAPI, bind


class Auth(SubclassAPI):

    login = bind(path='auth/login/',
        allowed_params=('fields', 'language', 'expires_at', 'redirect_uri', 'display', 'nofollow'),
        doc='''OpenID login

        :reference: https://wargaming.net/developers/api_reference/wot/auth/login/''')

    prolongate = bind(path='auth/prolongate/',
        allowed_params=('expires_at', 'access_token'),
        doc='''Access token extension
        :reference: https://wargaming.net/developers/api_reference/wot/auth/prolongate/''')

    logout = bind(path='auth/logout/',
        allowed_params=('access_token', ),
        doc='''Log out

        :reference: https://wargaming.net/developers/api_reference/wot/auth/logout/''')
