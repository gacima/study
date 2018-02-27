# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string


def cleanContent(content):
    content = re.sub("\n+", " ", content)
    content = re.sub("\[[0-9]*\]", "", content)
    content = re.sub(" +", " ", content)
    content = bytes(content, "UTF-8")
    content = content.decode("ascii", "ignore")
    cleanInput = []
    content = content.split(' ')
    for item in content:
        item = item.strip(string.punctuation) #所有标点字符,移除首尾的所有标点字符
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput


def ngrams(content, n):
    content = cleanContent(content)
    output = []
    for i in range(len(content) - n + 1):
        output.append(content[i:i+n])
    return output


html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html)
content = bsObj.find("div", {'id': "mw-content-text"}).get_text()
ngrams = ngrams(content, 2)
print(ngrams)
print("2-grams count is: " + str(len(ngrams)))