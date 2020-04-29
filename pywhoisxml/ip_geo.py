from pywhoisxml.conf import URL_DEFAULTS, get_response,return_value,get_balance
from pywhoisxml.exceptions import PyWhoisException

class IpGeo(object):
    def __init__(self,api_key,ip_address,output_format = "JSON",**kwargs):
        self.api_key = api_key
        self.ip_address  = ip_address
        self.code = 8
        self.url=URL_DEFAULTS.get('ip_address')
        self.params = {
            "apiKey":api_key,
            "outputFormat":output_format,
            "ipAddress" :self.ip_address

        }
        self.params.update(kwargs)
        self.response =get_response(self.url,self.params)
        self.filtered_response = self.response['location']
     
    @property
    def country(self):
        return return_value(self.filtered_response,'country') 
    @property    
    def balance(self): 
        return get_balance(self.api_key,self.code)       
    @property
    def region(self):
        return return_value(self.filtered_response,'region')
    @property
    def city(self):
        return return_value(self.filtered_response,'city')
    @property
    def latitude(self):
        return return_value(self.filtered_response,'lat')
    @property
    def longitude(self):
        return return_value(self.filtered_response,"long")
    @property
    def postal_code(self):
        return return_value(self.filtered_response,"postalCode")
    @property
    def time_zone(self):
        return return_value(self.filtered_response,"timezone")                    