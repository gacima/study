from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    links = bsObj.find('div', {'id': 'bodyContent'}).findAll('a', {'href': re.compile("^(/wiki/)((?!:).)*$")})
    return links


def getHistoryIps(pageUrl):
    #https://en.wikipedia.org/w/index.php?title=Programming_paradigm&action=history
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "https://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
    print(historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html)
    ipaddresses = bsObj.findAll("a", {"class": "mw-userlink mw-anonuserlink"})
    addressList = set()
    for ipaddress in ipaddresses:
        addressList.add(ipaddress.get_text())
    return addressList


links = getLinks("/wiki/Python_(programming_language)")

if __name__ == "__main__":
    while len(links) > 0:
        for link in links:
            print(link)
            historyIps = getHistoryIps(link.attrs['href'])
            for historyIp in historyIps:
                print(historyIp)

        newLink = links[random.randint(0, len(links) - 1)].attrs['href']
        links = getLinks(newLink)