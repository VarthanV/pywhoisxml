from pywhoisxml.conf import URL_DEFAULTS, get_response, return_value,get_balance
from pywhoisxml.exceptions import PyWhoisException


class DomainReputation(object):
    def __init__(self, api_key, domain, output_format="JSON", **kwargs):
        self.api_key = api_key
        self.domain = domain
        self.code = 20
        self.url = URL_DEFAULTS.get('reputation')
        self.params = {
            "apiKey": api_key,
            "outputFormat": output_format,
            "domainName": domain

        }
        self.params.update(kwargs)
        self.response = get_response(self.url, self.params)
    @property
    def data(self):
         return self.response   
    @property
    def score(self):
        return return_value(self.response,"reputationScore")
    @property    
    def balance(self): 
        return get_balance(self.api_key,self.code)       
