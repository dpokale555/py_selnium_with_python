import os
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)

#This is existing in selenium 4
reglink=Keys.CONTROL+Keys.RETURN
driver.find_element(By.XPATH,"//a[@class='ico-register']").send_keys(reglink)
time.sleep(4)

#This is new feature in selenium 4: open the new tab
driver2 = webdriver.Chrome()
driver2.get("https://demo.nopcommerce.com/")
driver2.switch_to.new_window('tab')
driver2.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver2.maximize_window()
driver2.implicitly_wait(10)

time.sleep(4)

#This is new feature in selenium 4: open the new tab in new browser
driver3 = webdriver.Chrome()
driver3.get("https://demo.nopcommerce.com/")
driver3.switch_to.new_window('window')
driver3.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver3.maximize_window()
driver3.implicitly_wait(10)

time.sleep(4)
driver.quit()