# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql, datetime, re, random

conn = pymysql.connect(host='127.0.0.1', user='root', password='root',
                       db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE test")

random.seed(datetime.datetime.now())


def store(title, content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")", (title, content))
    cur.connection.commit()


def getLinks(articl_url):
    html = urlopen('http://en.wikipedia.org' + articl_url)
    bsObj = BeautifulSoup(html)
    # start save date to database
    title = bsObj.find('h1').get_text()
    content = bsObj.find('div', id='mw-content-text').get_text()[:20]
    store(title, content)
    # end
    return bsObj.find('div', id='bodyContent').findAll('a', href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Kevin_Bacon")
try:
    while len(links) > 0:
        new_aticle_url = links[random.randint(0, len(links) - 1)]['href']
        print(new_aticle_url)
        getLinks(new_aticle_url)
finally:
    cur.close()
    conn.close()