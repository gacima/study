# -*- coding: utf-8 -*-
from urllib.request import urlopen

text = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(str(text.read(), 'utf-8'))