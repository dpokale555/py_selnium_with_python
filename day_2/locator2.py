from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()

#Class Name Locator
sliders=driver.find_elements(By.CLASS_NAME, "homeslider-container")
print("Total No of images in slider :",len(sliders))

#Tag name
links=driver.find_elements(By.TAG_NAME, "a")
print("Total No of links on Homepage :",len(links))

#