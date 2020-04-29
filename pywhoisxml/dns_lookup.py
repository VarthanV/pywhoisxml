from pywhoisxml.conf import URL_DEFAULTS, get_response, return_value, get_balance
from pywhoisxml.exceptions import PyWhoisException


class DnsLookup(object):
    def __init__(self, api_key, domain, output_format="JSON", **kwargs):
        self.domain = domain
        self.api_key = api_key
        self.code = 26
        self.url = URL_DEFAULTS.get("dns_lookup")
        self.params = {
            "apiKey": self.api_key,
            "outputFormat": output_format,
            "domainName": domain

        }
        self.params.update(kwargs)
        self.response = get_response(self.url, self.params)
    @property    
    def balance(self): 
        return get_balance(self.api_key,self.code)       

    @property
    def types(self):
        return get_response(self.response, 'types')

    @property
    def dns_records(self):
        return get_response(self.response, 'dnsRecords')
