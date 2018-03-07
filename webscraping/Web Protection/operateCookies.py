# -*- coding: utf-8 -*-
from selenium import webdriver

phantomjs_path = 'D:/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe'

#driver1先登录网站
driver1 = webdriver.PhantomJS(executable_path=phantomjs_path)
driver1.get('https://github.com')
driver1.implicitly_wait(2)
print(driver1.get_cookies())
savedCookies = driver1.get_cookies()

#driver2再登录网站，删除所有cookies
driver2 = webdriver.PhantomJS(executable_path=phantomjs_path)
driver2.get('https://github.com')
driver2.delete_all_cookies()
print(driver2.get_cookies())
for cookie in savedCookies:
    driver2.add_cookie(cookie)

print("~~" * 10)

driver2.get('https://github.com')
driver2.implicitly_wait(2)
print(driver2.get_cookies())