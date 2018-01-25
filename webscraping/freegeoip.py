import json
from urllib.request import urlopen


def getCountry(ipAdress):
    response = urlopen('http://freegeoip.net/json/' + ipAdress).read().decode('utf-8')
    responseJson = json.loads(response)
    print(responseJson)
    return responseJson.get('country_code') + " " + responseJson.get('city')


print(getCountry('50.78.253.58'))