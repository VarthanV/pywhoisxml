from pywhoisxml.exceptions import PyWhoisException
import requests

class Auth(object):
    def __init__(self, api_key, code):
        self.api_key = api_key
        self.code = code

    @property
    def balance(self):
        res = requests.get(
            "https://user.whoisxmlapi.com/service/account-balance", params={"apiKey": self.api_key}).json()
        res = res.get('data')
        for item in res:
         if item['product_id'] == self.code:
            return item.get('credits')
        return None
