from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
imgLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
print(imgLocation)
urlretrieve(imgLocation, "logo.jpg")