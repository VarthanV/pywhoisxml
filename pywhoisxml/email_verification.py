from pywhoisxml.conf import URL_DEFAULTS, get_response,return_value
from pywhoisxml.exceptions import PyWhoisException


class EmailVerification(object):
    def __init__(self, api_key, email,output_format="JSON",**kwargs):
        self.api_key =api_key
        self.url = URL_DEFAULTS.get("email_verification")
        self.params = {
            "apiKey": self.api_key,
            "outputFormat": output_format,
            "emailAddress": email
        }
        self.params.update(kwargs)
        self.response = get_response(self.url, self.params)

    @property
    def data(self):
        return self.response

    @property
    def format_check(self):
        return bool(return_value(self.response,'formatCheck'))

    @property
    def smtp_check(self):
        return bool(return_value(self.response,'smtpCheck'))

    @property
    def dns_check(self):
        return bool(return_value(self.response,'dnsCheck'))

    @property
    def catch_all_checks(self):
        return bool(return_value(self.response,'catchAllCheck'))
