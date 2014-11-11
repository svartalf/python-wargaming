# -*- coding: utf-8 -*-


class APIError(Exception):
    pass


class RequestError(APIError):

    def __init__(self, code, field, message='', value=''):
        self.status_code = code
        self.field = field
        self.message = message
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return '<Request error: {}>'.format(self.message)


class ValidationError(APIError):
    pass
