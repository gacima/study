import os
from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup

downloadFolder = "D:/downloaded"
baseUrl = "http://pythonscraping.com"


def getAbsoluteURL(baseUrl, source):
    if source.startswith('http://www.'):
        url = "http://" + source[11:]
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = 'http://' + source[4:]
    else:
        url = baseUrl + "/" + source
    if "?" in url:
        url = url[:url.find('?')]
    if baseUrl not in url:
        return None
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadFolder):
    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    path = downloadFolder + path
    folder = os.path.dirname(path)

    if not os.path.exists(folder):
        os.makedirs(folder)

    return path


html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
downloadList = bsObj.find_all(src=True)

for download in downloadList:
    #print(download['src'] + "    **********")
    fileUrl = getAbsoluteURL(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadFolder))