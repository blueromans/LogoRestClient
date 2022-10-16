import requests

from logorestclient.exceptions import LogoException
from logorestclient.serializer import Serializer


class HttpService:
    REST_URL = None

    def __init__(self, REST_URL):
        if REST_URL is None:
            raise LogoException("REST_URL required!")
        self.REST_URL = REST_URL

    def connect(self, method, url, request_body=None, headers=None, is_json=False):
        if request_body is None:
            request_body = {}
        if method == 'GET':
            r = requests.get(self.REST_URL + url, headers=headers)
        elif method == 'POST':
            if is_json is True:
                request_body = Serializer.dumps(request_body)
            r = requests.post(self.REST_URL + url, data=request_body, headers=headers)
        res = r.text.encode('utf-8')
        res = Serializer.loads(res)
        if 'Meta' in res:
            del res['Meta']
        return res
