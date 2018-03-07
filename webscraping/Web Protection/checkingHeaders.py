# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

session = requests.session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
           , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
url = 'https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending'
req = session.get(url, headers=headers)
bsObj = BeautifulSoup(req.text)
print(bsObj.find("table", {'class': 'table-striped'}).get_text)