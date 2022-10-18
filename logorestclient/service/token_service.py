import datetime

from logorestclient.exceptions import LogoException
from logorestclient.helper.sqlite import initialize_sql_lite
from logorestclient.helper.token import get_token, update_token
from logorestclient.service.http_service import HttpService


class TokenService(HttpService):
    def __init__(self, REST_URL, **payloads):
        if payloads is None:
            raise LogoException("Payloads required!")
        super().__init__(REST_URL)
        self.payloads = payloads
        initialize_sql_lite()
        self.token_dict = get_token()
        if self.token_dict is None:
            self.token_dict = self.retrieve_access_token()
            return
        self.token_expire_date = datetime.datetime.strptime(self.token_dict['.expires'], '%a, %d %b %Y %H:%M:%S GMT')
        if datetime.datetime.now() < self.token_expire_date:
            return
        self.token_dict = self.retrieve_access_token()

    def retrieve_access_token(self):
        res = self.connect('POST', '/api/v1/token', self.payloads)
        if 'error' in res:
            raise LogoException(res['error'] + ' ' + res['error_description'])
        update_token(res)
        return res
