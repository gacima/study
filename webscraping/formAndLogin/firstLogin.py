import requests

#params = {"firstname": "Ryan", "lastname": "Mitchell"}
#r = requests.post("http://www.pythonscraping.com/pages/files/processing.php", data=params)
#print(r.text)

params = {'email_addr': "ryan.e.mitchell@gmail.com"}
r = requests.post("http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi", data=params)
print(r.text)