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

        for endpoint in endpoints:
            fun = self.__make_endpoint_fun(endpoint)
            setattr(self, endpoint.replace('/', '_'), fun)

    def __make_endpoint_fun(self, name):
        def _function(**kwargs):
            options={}
            options.update({
                't': kwargs.get('taxon', ''),
                'l': kwargs.get('location', ''),
                'c': kwargs.get('code', ''),
                'd': kwargs.get('date_range', ''),
                'q': kwargs.get('other', ''),
                'p': kwargs.get('geo', ''),
                'm': kwargs.get('map', '')
            })
            return self.get('{}/'.format(name), options)
        return _function

    def _update_options(options, **kwargs):
            options.update({'t': kwargs.get})

    def get(self, request, options):
        options.update({'api': self.api_key})
        url = '{}{}?{}'.format(self.base_url, request, urlencode(options))
        return urlopen(url)