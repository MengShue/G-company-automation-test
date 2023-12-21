import requests
import json
from contextlib import closing


class HttpClient(object):

    def __init__(self, protocol=None, fqdn=None):  # Given a default link to verify http function.
        self.protocol = protocol if protocol is not None else 'https://'
        self.fqdn = fqdn if fqdn is not None else 'api.github.com/'
        self.url = self.protocol + self.fqdn

    def http_request(self, url=None, api_path=None, method='GET', header=None, parameter=None, payload=None):
        api_path = '' if api_path is None else api_path
        # if url pass, use url, ignore api_path
        url = self.url + api_path if url is None else url
        payload = None if payload is None or payload == "" else payload
        res = None
        if method.upper() == 'GET':
            res = self._get_request(api_path=url, header=header, parameter=parameter, payload=payload)
        elif method.upper() == 'POST':
            res = self._post_request(api_path=url, header=header, parameter=parameter, payload=payload)
        elif method.upper() == 'PUT':
            res = self._put_request(api_path=url, header=header, parameter=parameter, payload=payload)
        elif method.upper() == 'DELETE':
            res = self._delete_request(api_path=url, header=header, parameter=parameter, payload=payload)
        print('Creating http request using : [url]=%s, [method]=%s\n[headers]=%s\n[parameter]=%s\n[payload]=%s' % (
                url, method, header, parameter, payload))
        try:
            body = res.content.decode("utf-8")
        except UnicodeDecodeError:
            body = res.content.decode("big5")
        body = body[0:1000] + "...... res content is too long, ignore message behind." if len(body) > 1000 else body
        print('Http response : [url]=%s, [status_code]=%s\n[headers]=%s\n[body]=%s' % (
            res.url, res.status_code, res.headers, body))
        res.close()

        return res

    @staticmethod
    def _get_request(api_path, header=None, parameter=None, payload=None):
        with closing(requests.get(api_path, headers=header, params=parameter, data=payload, stream=False)) as res:
            return res

    @staticmethod
    def _post_request(api_path, header=None, parameter=None, payload=None):
        with closing(requests.post(api_path, headers=header, params=parameter, data=payload, stream=False)) as res:
            return res

    @staticmethod
    def _put_request(api_path, header=None, parameter=None, payload=None):
        with closing(requests.put(api_path, headers=header, params=parameter, data=payload, stream=False)) as res:
            return res

    @staticmethod
    def _delete_request(api_path, header=None, parameter=None, payload=None):
        with closing(requests.delete(api_path, headers=header, params=parameter, data=payload, stream=False)) as res:
            return res

    @staticmethod
    def _string_to_json(content):
        res = json.loads(content)
        return res


if __name__ == "__main__":
    print("httpClient.py is running directly")
    hc = HttpClient('https://', 'api.github.com/')
    r = hc.http_request('events')
    print(r.status_code)
    print(r.json())
