import json
from urllib.request import urlopen
from webscraping import historyIpsScraping as hi

def getCountry(ipAdress):
    response = urlopen('http://freegeoip.net/json/' + ipAdress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get('country_code') + " " + responseJson.get('city')


#print(getCountry('50.78.253.58'))
links = hi.getLinks("/wiki/Python_(programming_language)")
if __name__ == "__main__":
    for link in links:
        ips = hi.getHistoryIps(link.attrs["href"])
        for ip in ips:
            location = getCountry(ip)
            print(location)