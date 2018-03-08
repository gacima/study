# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get('http://www.pythonscraping.com/pages/javascript/draggableDemo.html')
print(driver.find_element_by_id('message').text)

element = driver.find_element_by_id('message')
target = driver.find_element_by_id('div2')
actions = ActionChains(driver)
actions.drag_and_drop(element, target).perform()
print(driver.find_element_by_id('message').text)