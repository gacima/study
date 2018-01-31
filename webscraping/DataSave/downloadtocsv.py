import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html)
#find the first table on the page
table = bsObj.find_all('table',  {'class': 'wikitable sortable'})[0]
rows = table.find_all('tr')

csvFile = open('../files/editors.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()