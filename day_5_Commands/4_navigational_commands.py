from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()

driver.get("https://www.snapdeal.com/")
time.sleep(3)

driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()


driver.quit()

