from pywhoisxml.conf import URL_DEFAULTS, get_response
from pywhoisxml.auth import Auth
from pywhoisxml.exceptions import PyWhoisException


class EmailVerification(Auth):
    def __init__(self, api_key, email):
        super().__init__(api_key)
        self.url = URL_DEFAULTS.get("email_verification")
        self.params = {
            "apiKey": self.api_key,
            "outputFormat": "JSON",
            "emailAddress": email
        }
        self.response = get_response(self.url, self.params)

    @property
    def data(self):
        return self.response

    def return_value(self, key):
        return bool(self.response.get(key))

    @property
    def format_check(self):
        return self.return_value('formatCheck')

    @property
    def smtp_check(self):
        return self.return_value('smtpCheck')

    @property
    def dns_check(self):
        return self.return_value('dnsCheck')

    @property
    def catch_all_checks(self):
        return self.return_value('catchAllCheck')
