# -*- coding: utf-8 -*-


class APIError(Exception):
    """Basic API error"""

    pass


class RequestError(APIError):
    """API request error

    Raises if Wargaming API returns error
    """

    def __init__(self, code, field, message, value):
        self.status_code = code
        self.field = field
        self.message = message
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return '<Request error: {0}>'.format(self.message)


class ValidationError(APIError):
    """Invalid param value error"""

    pass
