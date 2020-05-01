### pywhoisxml

This Library is a wrapper for  [Whois Xml](https://www.whoisxmlapi.com/ "Whois Xml")   
api service . It offers many helper methods to get the commonly used data's easily.
## Installation

### From PyPI

```bash
pip install py3whoisxml
```
### Whois Lookup Usage


```python
from pywhoisxml.lookup import Lookup
l =Lookup('<API KEY>','vishnurao.tech')
print(l.is_available)
#Returns False as the Domain is Unavailable 
print(l.data)
# Returns the JSON Response Received from the API
print(l.balance)
#Returns the balance no if requests you can make to the API 
#Eg : 498
```

## Email Verification API

```python
from pywhoisxml.email_verification import  EmailVerification
e =EmailVerification('<API KEY>','test@gmail.com')
print(e.format_check)
#Returns whether the above check is passed

```

## IP Geolocation API

```python
from pywhoisxml.ip_geo import IpGeo
 e =IpGeo('<API KEY>',  '<IP> ')
 print(e.region)
# Returns the region of the IP
print(e.country)
# Returns the Country of the  IP

```



