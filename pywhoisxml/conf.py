import requests
from pywhoisxml.exceptions import PyWhoisException
URL_DEFAULTS = {
    "lookup_url": "https://www.whoisxmlapi.com/whoisserver/WhoisService",
    "email_verification":"https://emailverification.whoisxmlapi.com/api/v1"
}


def get_response(url, params):
    response = requests.get(url, params=params)
    response = response.json()

    if not 'Error' in response:
        return response
    else :    
      raise PyWhoisException(
        "Make sure you have passed the right params ,Please Try again later")
  