# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get('https://www.baidu.com')
driver.get_screenshot_as_file('baidu.png')