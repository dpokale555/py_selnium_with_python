import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
driver.maximize_window()

drp_elment=driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select")
drpcountry=Select(drp_elment)

#1)select the option from the dropdown
drpcountry.select_by_visible_text("Austria")
time.sleep(3)
drpcountry.select_by_value("BES")
time.sleep(3)
drpcountry.select_by_index(5)
time.sleep(3)


#2)Captured all the options and print in console
all_options=drpcountry.options
print("Total list :",len(all_options))

for country in all_options:
    print(country.text)


#3) Select the options from dropdown without using built in fucntion
for ops in all_options:
    if ops.text=="Bhutan":
        ops.click()
        print(ops)
        break

time.sleep(3)

driver.close()
