from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Single Iframe']").click()
driver.switch_to.frame("SingleFrame")
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Hello")
time.sleep(3)
driver.switch_to.default_content()

#What if name,id of the frame is not avalaible so using webelement will do (inner_iframes)
print("multiframe start")
driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
outer_iframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_iframe)
inner_iframe=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(inner_iframe)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Hello")
print("multiframe end")
time.sleep(3)

#swithc to parent frame
driver.switch_to.parent_frame()
