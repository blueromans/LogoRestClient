# LogoRestClient PyPackage

## Requirements

* [Python ^3.6.4](https://www.python.org/downloads/release/python-380)

## Setup

```bash
pip install LogoRestClient
```

## Usage

### Credentials

```bash
{
  'LOGO_REST_API': 'api url', 
  'LOGO_USER_NAME': 'username', 
  'LOGO_USER_PASSWORD': 'password',
  'LOGO_GRANT_TYPE': 'grant type', 
  'LOGO_CLIENT_ID': 'client id', 
  'LOGO_CLIENT_NUMBER': 'client number',
  'LOGO_CLIENT_SECRET': 'client secret'
}
```
### Initialize

```bash
from logorestclient import LogoService
logo_service = LogoService(credentials)
result = logo_service.runQuery('sql_query') 
```
