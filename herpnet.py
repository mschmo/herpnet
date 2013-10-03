# Forced to use urllib instead of requests
# Requests gives back an IncompleteRead exception (from httplib)
from urllib import urlopen, urlencode

endpoints = ['taxa', 'providers', 'occurrencecount',
                 'occurrence', 'availablemaps', 'locations']


class Herpnet:
    api_key = ''
    base_url = 'http://www.herpnet2.org/api/v1/'

    def __init__(self, api_key):
        self.api_key = api_key

        for endpoint in get_endpoints:
            fun = self.__make_get_endpoint_fun(endpoint)
            setattr(self, endpoint.replace('/', '_'), fun)

    def __make_endpoint_fun(self, name):
        def _function(options={}):
            return self.get('{}/'.format(name), options)
        return _function

    def get(self, request, options):
        options.update({'api': self.api_key})
        url = '{}{}?{}'.format(self.base_url, request, urlencode(options))
        return urlopen(url)