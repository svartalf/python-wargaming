# -*- coding: utf-8 -*-


class APIError(Exception):
    """Basic API error"""

    pass


class RequestError(APIError):
    """API request error

    Raises if Wargaming API returns error
    """

    def __init__(self, code, field, message, value):
        super(RequestError, self).__init__(message)
        self.code = code
        self.field = field
        self.message = message
        self.value = value


class ValidationError(APIError):
    """Invalid param value error"""

    pass
