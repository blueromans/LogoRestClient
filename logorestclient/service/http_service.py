import requests

from logorestclient.exceptions import LogoException
from logorestclient.serializer import Serializer


class HttpService:
    REST_URL = None

    def __init__(self, REST_URL):
        if REST_URL is None:
            raise LogoException("REST_URL required!")
        self.REST_URL = REST_URL

    @staticmethod
    def parse_result(r):
        res = r.text.encode('utf-8')
        res = Serializer.loads(res)
        if 'Meta' in res:
            del res['Meta']
        return res

    def post_request(self, url, request_body, headers, is_json):
        if is_json is True:
            request_body = Serializer.dumps(request_body)
        r = requests.post(url, data=request_body, headers=headers)
        return self.parse_result(r)

    def get_request(self, url, headers):
        r = requests.get(url, headers=headers)
        return self.parse_result(r)

    def connect(self, method, url, request_body={}, headers=None, is_json=False):
        if method == 'GET':
            return self.get_request(self.REST_URL + url, headers)
        return self.post_request(self.REST_URL + url, request_body, headers, is_json)