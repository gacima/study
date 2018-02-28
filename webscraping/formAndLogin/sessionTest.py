import requests

session = requests.Session()
params = {"username": "test", "password": "password"}
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print(s.text)
print("~~" * 10)
print("and the cookies is set to")
print(s.cookies)
print("~~" * 10)
print("Going to profile page")
r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(r.text)