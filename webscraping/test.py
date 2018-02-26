# -*- coding: utf-8 -*-
from urllib.parse import urlparse

parseurl = urlparse("http://www.baidu.com")
print(parseurl)
print(parseurl.netloc)