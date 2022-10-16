# LogoRestClient PyPackage

LogoRestClient is a Python library for accessing logo rest.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install LogoRestClient
```

## Usage

```python
from logorestclient import LogoService

credentials {
  'LOGO_REST_API': 'api url', 
  'LOGO_USER_NAME': 'username', 
  'LOGO_USER_PASSWORD': 'password',
  'LOGO_GRANT_TYPE': 'grant type', 
  'LOGO_CLIENT_ID': 'client id', 
  'LOGO_CLIENT_NUMBER': 'client number',
  'LOGO_CLIENT_SECRET': 'client secret'
}
logo_service = LogoService(credentials)
# returns 'query result'
result = logo_service.runQuery('sql_query') 

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)