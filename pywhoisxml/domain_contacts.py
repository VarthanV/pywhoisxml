from pywhoisxml.conf import URL_DEFAULTS, get_response, return_value, get_balance
from pywhoisxml.exceptions import PyWhoisException


class DomainContacts(object):
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
    def company_names(self):
        return return_value(self.response, 'companyNames')

    @property
    def emails(self):
        return return_value(self.response, "emails")

    @property
    def description(self):
        return self.response['meta']['description']

    @property
    def facebook_link(self):
        return self.response['socialLinks']['facebook']

    @property
    def instagram_link(self):
        return self.response['socialLinks']['instagram']

    @property
    def linkedin_link(self):
        return self.response['socialLinks']['linkedIn']

    @property
    def twitter_link(self):
        return self.response['socialLinks']['twitter']

    @property
    def balance(self):
        return get_balance(self.api_key, self.code)
