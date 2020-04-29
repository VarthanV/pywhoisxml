from pywhoisxml.conf import URL_DEFAULTS, get_response, return_value
from pywhoisxml.exceptions import PyWhoisException
from pywhoisxml.auth import Auth


class IpGeo(Auth):
    def __init__(self, api_key, ip_address, output_format="JSON", **kwargs):
        self.code = 8
        super().__init__(api_key, self.code)
        self.ip_address = ip_address

        self.url = URL_DEFAULTS.get('ip_address')
        self.params = {
            "apiKey": api_key,
            "outputFormat": output_format,
            "ipAddress": self.ip_address

        }
        self.params.update(kwargs)
        self.response = get_response(self.url, self.params)
        self.filtered_response = self.response['location']

    @property
    def country(self):
        return return_value(self.filtered_response, 'country')

    @property
    def region(self):
        return return_value(self.filtered_response, 'region')

    @property
    def city(self):
        return return_value(self.filtered_response, 'city')

    @property
    def latitude(self):
        return return_value(self.filtered_response, 'lat')

    @property
    def longitude(self):
        return return_value(self.filtered_response, "long")

    @property
    def postal_code(self):
        return return_value(self.filtered_response, "postalCode")

    @property
    def time_zone(self):
        return return_value(self.filtered_response, "timezone")
