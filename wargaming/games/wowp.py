# -*- coding: utf-8 -*-

from wargaming.api import BaseAPI


class API(BaseAPI):

    def __init__(self, application_id, base_url='https://api.worldofwarplanes.com/wowp/'):
        super(API, self).__init__(application_id, base_url)
