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

#Capture cookies from the browser
Browser_cookies=driver.get_cookies()
print("Total Number of cookies",len(Browser_cookies))

#Print the deatils of all cookies
for c in Browser_cookies:
    print(c)
    print(c.get('name'),":",c.get('expiry'))

#Add new cookies to the browser
driver.add_cookie({"name" : "My Cookie1", "value" : "13223"})
Bwsr_latst_Cookies=driver.get_cookies()
print("Total Number of cookies after adding new cookie:",len(Bwsr_latst_Cookies))

#Delet the specific cookie from the browser
driver.delete_cookie('My Cookie1')
Bwsr_delt_Cookies=driver.get_cookies()
print("Total Number of cookies after deleting new cookie:",len(Bwsr_delt_Cookies))


driver.quit()