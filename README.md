# LogoRestClient PyPackage

Logo is the most popular Erp desktop application at Turkey. LogoRestClient is a Python library to access logo rest services quickly.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install LogoRestClient
```

## Usage

```python
from logorestclient import LogoService

credentials = {
    'GRANT_TYPE': 'grant type',
    'USER_NAME': 'username',
    'CLIENT_NUMBER': 'client number',
    'PASSWORD': 'password',
    'REST_URL': 'rest url',
}
logo_service = LogoService(credentials)
# returns 'query result'
result = logo_service.runQuery('sql_query')

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
