from pywhoisxml.conf import URL_DEFAULTS, get_response, return_value
from pywhoisxml.exceptions import PyWhoisException
from pywhoisxml.auth import Auth


class DnsLookup(Auth):
    def __init__(self, api_key, domain, output_format="JSON", **kwargs):
        self.code = 26
        super(Auth).__init__(api_key, self.code)
        self.domain = domain

        self.url = URL_DEFAULTS.get("dns_lookup")
        self.params = {
            "apiKey": self.api_key,
            "outputFormat": output_format,
            "domainName": domain

        }
        self.params.update(kwargs)
        self.response = get_response(self.url, self.params)

    @property
    def types(self):
        return get_response(self.response, 'types')

    @property
    def dns_records(self):
        return get_response(self.response, 'dnsRecords')
