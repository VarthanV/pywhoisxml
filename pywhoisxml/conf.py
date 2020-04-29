import requests
from pywhoisxml.exceptions import PyWhoisException
URL_DEFAULTS = {
    "lookup_url": "https://www.whoisxmlapi.com/whoisserver/WhoisService"
}


def get_response(url, params):
    response = requests.get(url, params=params)
    response = response.json()

    if not 'ErrorCode' in response:
        return response
    raise PyWhoisException(
        "Make sure you have passed the right params ,Please Try again later")
