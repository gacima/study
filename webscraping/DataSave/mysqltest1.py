# -*- coding: utf-8 -*-
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='mysql')
cur = conn.cursor()
cur.execute('USE forta')

cur.execute('SELECT * FROM vendors')
print(cur.fetchall())
cur.close()
conn.close()