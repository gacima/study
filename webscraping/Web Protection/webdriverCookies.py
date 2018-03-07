# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get('http://www.baidu.com')
driver.implicitly_wait(3)
print(driver.get_cookies())