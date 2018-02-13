# -*- coding: utf-8 -*-
import csv
from io import StringIO
from urllib.request import urlopen

data = urlopen("http://www.pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
# arg---'ignore' will ignore the illegal character
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)

for row in csvReader:
    print(row)

print("~~" * 10)

data1 = urlopen("http://www.pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('utf-8', 'ignore')
dataFile1 = StringIO(data1)
csvDictReader = csv.DictReader(dataFile1)

print(csvDictReader.fieldnames)
for row in csvDictReader:
    print(row)