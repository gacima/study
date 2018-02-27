# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, string, operator


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


def ngrams(input, n):
    content = cleanContent(input)
    output = {}
    for i in range(len(content)-n+1):
        ngramTemp = " ".join(content[i:i+n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output


content = str(urlopen("http://www.pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
ngrams = ngrams(content, 2)
print(ngrams)
sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(sortedNGrams)