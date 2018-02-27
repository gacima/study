# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import string
import re


def split(content):
    content = re.sub("\n+", " ", content)
    content = re.sub("\[[0-9]*\]", "", content)
    content = re.sub(" +", " ", content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    cleanedwords = []
    content = content.split(" ")
    for item in content:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item == "i" or item == "a"):
            cleanedwords.append(item)
    return cleanedwords


html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html)
content = bsObj.find("div", {'id': "mw-content-text"}).get_text()
words = split(content)
print(words)
print(len(words))