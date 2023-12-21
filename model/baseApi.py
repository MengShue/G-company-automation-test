from module.httpUtils.httpClient import HttpClient


class BaseApi(object):

    def __init__(self, protocol=None, fqdn=None, path=None):
        self.protocol = protocol if protocol is not None else 'https://'
        self.fqdn = fqdn if fqdn is not None else 'swapi.dev/'
        self.path = path if path is not None else ''
        self.url = self.protocol + self.fqdn + self.path
        self.httpClient = HttpClient(self.protocol, self.fqdn + self.path)

    def get_api(self):
        res = self.httpClient.http_request(api_path='api', method='GET')
        return res


if __name__ == "__main__":  # For quick debug
    print("baseApi.py is running directly")
    api = BaseApi()
    r = api.get_api()
    print(r.status_code)
    print(r.json())
