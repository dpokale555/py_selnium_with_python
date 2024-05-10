from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/login")
driver.maximize_window()
time.sleep(2)
emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")
emailbox.clear()
emailbox.send_keys("xyz@gmail.com")
print("result of text :",emailbox.text)
print("result of GetAttribute of Value :",emailbox.get_attribute('value'))

login_btn=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("result of text :",login_btn.text)
print("result of GetAttribute of Value :",login_btn.get_attribute('value'))
print("result of GetAttribute of Value :",login_btn.get_attribute('type'))
