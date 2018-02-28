import requests

files = {"uploadFile": open("J:/test.jpg", 'rb')}
r = requests.post("http://www.pythonscraping.com/pages/processing2.php", files=files)
print(r.text)