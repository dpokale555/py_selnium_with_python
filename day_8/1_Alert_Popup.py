from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

js_alert=driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
js_prompt=driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
js_prompt.click()

alert_window=driver.switch_to.alert
print(alert_window.text)
time.sleep(2)
alert_window.send_keys("Hello")
time.sleep(2)
alert_window.accept()
time.sleep(2)
# alert_window.dismiss()

js_alert.click()
alert_window2=driver.switch_to.alert
print(alert_window2.text)
time.sleep(2)
alert_window2.accept()
time.sleep(2)


