from logorestclient.exceptions import LogoException
from logorestclient.service.token_service import TokenService


class LogoService(TokenService):
    def __init__(self, credentials):
        if credentials is None:
            raise LogoException("Credentials required!")
        payload = {
            'grant_type': credentials['GRANT_TYPE'],
            'username': credentials['USER_NAME'],
            'firmno': credentials['CLIENT_NUMBER'],
            'password': credentials['PASSWORD']
        }
        super().__init__(credentials['REST_URL'], **payload)
        token = self.token_dict['access_token']
        self.headers = {
            'Authorization': f'Bearer {token}',
            'content-type': 'application/json',
            'accept': 'application/json'
        }

    def runQuery(self, query):
        res = self.connect('GET', '/api/v1/queries?tsql=' + query, headers=self.headers)
        if 'error' in res:
            raise LogoException(res['error'] + ' ' + res['error_description'])
        if 'Message' in res and 'ModelState' in res:
            if '207' in res['ModelState']:
                raise LogoException(res['ModelState']['207'])
            if 'LoginError' in res['ModelState']:
                token_dict = self.retrieve_access_token()
                self.token_dict = token_dict
                return self.runQuery(query)
        if 'count' in res and res['count'] == 0 or len(res['items']) == 0:
            return
        return res
