from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()

print(driver.title)