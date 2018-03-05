# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.common.exceptions import StaleElementReferenceException


def wait_for_load(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("After 10 seconds the page will returning.")
            return
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return


driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get("http://www.pythonscraping.com/pages/javascript/redirectDemo1.html")
wait_for_load(driver)
print(driver.page_source)