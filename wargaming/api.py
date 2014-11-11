# -*- coding: utf-8 -*-

from six.moves.urllib.parse import urlparse, urlunparse, urljoin, urlencode

from wargaming import settings
from wargaming.exceptions import ValidationError


class BaseAPI(object):

    def __init__(self, application_id, base_url):
        self.application_id = application_id

        url_parts = urlparse(base_url)
        self.url_scheme = url_parts.scheme
        self.url_netloc = url_parts.netloc
        self.url_path = url_parts.path

    def _get_url(self, path, parameters):
        return urlunparse([
            self.url_scheme,
            self.url_netloc,
            urljoin(self.url_path, path),
            None,
            urlencode(parameters),
            None
        ])

    @staticmethod
    def prepare_language(value):
        """Localization language

        One of the :data:`wargaming.settings.ALLOWED_LANGUAGES`
        """

        if value not in settings.ALLOWED_LANGUAGES:
            raise ValidationError('Invalid language: {}'.format(value))

        return value

    @staticmethod
    def prepare_fields(value):
        """List of response fields

        Fields are separated by commas. Nested fields are separated by dots."""

        if value:
            return ','.join(value)

        return ''
