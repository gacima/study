# -*- coding: utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get("http://www.pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(10)
print(driver.find_element_by_id("content").text)
driver.close()