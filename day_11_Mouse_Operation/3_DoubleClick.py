from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame('iframeResult')

filed1=driver.find_element(By.XPATH,"//input[@id='field1']")
filed2=driver.find_element(By.XPATH,"//input[@id='field2']")
button=driver.find_element(By.XPATH,"//button[@ondblclick='myFunction()']")

act=ActionChains(driver)
act.double_click(button).perform()


time.sleep(4)