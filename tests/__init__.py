import unittest2 as unittest

from wargaming.exceptions import APIError


class WargamingTestCase(unittest.TestCase):

    api_class = None

    def setUp(self):
        if self.api_class is None:
            raise RuntimeError('Invalid API class')

        self.api = self.api_class(application_id='demo')

    def assertValidResponse(self, method, **kwargs):
        try:
            response = method(**kwargs)
        except APIError as e:
            self.fail('Method {0} returns error response: {1}'.format(method, e.message))
