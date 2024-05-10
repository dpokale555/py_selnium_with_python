from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#1) Clicking on links
driver.find_element(By.LINK_TEXT,"Digital downloads").click()

#2) finds total numbers of links on a page
total_links=driver.find_elements(By.TAG_NAME,'a')
# total_links=driver.find_elements(By.XPATH,"//a")
print(len(total_links))

for link in total_links:
    print(link.text)