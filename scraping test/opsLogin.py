# -*- coding: utf-8 -*-
from urllib.request import urlopen
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get('http://172.31.170.37/sc/login.do')

loginNameFiled = driver.find_element_by_id('userName')
passwordFiled = driver.find_element_by_id('password')
loginBtnFiled = driver.find_element_by_id('btnLogin')

#点击登录
loginNameFiled.send_keys('guoying')
passwordFiled.send_keys('password1')
loginBtnFiled.click()
#driver.get_screenshot_as_file('success.jpg')

print(driver.get_cookies())
print(driver.h)