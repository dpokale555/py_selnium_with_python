from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

#Scrolling is not handled by using Action Class

driver = webdriver.Chrome()
driver.get("https://www.cs.cmu.edu/~bam/uicourse/2014inter/ScrollExperiment/sample1.htm")
driver.maximize_window()
driver.implicitly_wait(10)

#1) Scroll down page by pixel
driver.execute_script("window.scrollBy(0,3000)","")
value=driver.execute_script("return window.pageYOffset;")
print("Number of Pixel Move :",value)

#2) Scroll down page till webelement
next_button=driver.find_element(By.XPATH,"//strong[normalize-space()='Next']")
driver.execute_script("arguments[0].scrollIntoView();",next_button)
value2=driver.execute_script("return window.pageYOffset;")
print("Number of Pixel Move :",value2)

#3) Scroll till the end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value3=driver.execute_script("return window.pageYOffset;")
print("Number of Pixel Move :",value3)

time.sleep(3)