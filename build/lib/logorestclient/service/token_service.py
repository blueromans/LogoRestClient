import datetime

from logorestclient.exceptions import LogoException
from logorestclient.helper.sqlite import initialize_sql_lite
from logorestclient.helper.token import get_token, update_token
from logorestclient.service.http_service import HttpService


class TokenService(HttpService):
    def __init__(self, LOGO_REST_API, **payloads):
        if payloads is None:
            raise LogoException("Settings required!")
        super().__init__(LOGO_REST_API)
        self.payloads = payloads
        initialize_sql_lite()
        self.token_dict = get_token()
        if self.token_dict is None:
            self.token_dict = self.retrieve_access_token()
            update_token(self.token_dict)
            return
        self.token_expire_date = datetime.datetime.strptime(self.token_dict['.expires'], '%a, %d %b %Y %H:%M:%S GMT')
        if datetime.datetime.now() < self.token_expire_date:
            return
        self.token_dict = self.retrieve_access_token()
        update_token(self.token_dict)

    def retrieve_access_token(self):
        res = self.connect('POST', '/api/v1/token', self.payloads)
        if 'error' in res:
            raise LogoException(res['error'] + ' ' + res['error_description'])
        return res
