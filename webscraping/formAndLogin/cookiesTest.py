import requests

params = {"username": "user", "password": "password"}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print(r.text)
print("~" * 20)
print("and the cookies is set to: ")
print(r.cookies.get_dict())
print("~" * 20)
print("Going to profile page")
r = requests.post("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)