# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get('http://en.wikipedia.org/wiki/Monty_Python')
print(driver.title)
assert "Monty Python" in driver.title
driver.close()