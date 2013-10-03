import requests

get_endpoints = []


class Herpnet:
    api_key = ''
    base_url = 'http://www.herpnet2.org/api/v1/'

    def __init__(self, api_key):
        self.api_key = api_key

        for endpoint in get_endpoints:
            fun = self.__make_get_endpoint_fun(endpoint)
            setattr(self, endpoint.replace('/', '_'), fun)

    def __make_get_endpoint_fun(self, name):
        def _function(options={}):
            return self.get(request, options)
        return _function

    def get(self, request, options):
        options.update({'api_key': self.api_key)
        return requests.get(self.base_url + request, params=options).text