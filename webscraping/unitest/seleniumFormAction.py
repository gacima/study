# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get('http://www.pythonscraping.com/pages/files/form.html')

firstNameField = driver.find_element_by_name('firstname')
lastNameField = driver.find_element_by_name('lastname')
submitButton = driver.find_element_by_id('submit')

#第一种方法：sendkeys & click button
#firstNameField.send_keys('Ryan')
#lastNameField.send_keys('Mitchell')
#submitButton.click()

#第二种方法，action chain，send keys
actions = ActionChains(driver).click(firstNameField).send_keys('Ryan')\
    .click(lastNameField).send_keys('Mitchell')\
    .click(submitButton).send_keys(Keys.RETURN)
actions.perform()

###################################
print(driver.find_element_by_tag_name('body').text)
driver.close()