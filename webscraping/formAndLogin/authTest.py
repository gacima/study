import requests
from requests.auth import AuthBase, HTTPBasicAuth

auth = HTTPBasicAuth('gacima', 'password')
r = requests.post("http://pythonscraping.com/pages/auth/login.php", auth=auth)
print(r.text)