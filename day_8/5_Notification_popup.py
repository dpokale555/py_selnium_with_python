from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=ops)
driver.get("https://whatmylocation.com/")
driver.maximize_window()

#We have to do some browser setting to avoid "notification type popup)
