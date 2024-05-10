from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

#is_diplayed and is_enabled
serach_box=driver.find_element(By.ID,"small-search-box-form")
print("Display Status :",serach_box.is_displayed())
print("Enable Status :",serach_box.is_enabled())

#is_selected
rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")

print("Selected default Status :",rd_male.is_selected())
print("Selected default Status :",rd_female.is_selected())

rd_male.click()
print("After selecting male button")
print("Selected Status :",rd_male.is_selected())
print("Selected Status :",rd_female.is_selected())

rd_female.click()
print("After selecting female button")
print("Selected Status :",rd_male.is_selected())
print("Selected Status :",rd_female.is_selected())

