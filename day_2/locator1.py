from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
time.sleep(2)
driver.maximize_window()
driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
time.sleep(2)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[2]/div[2]/form[1]/button[1]").click()
time.sleep(2)

#LinkText locator
driver.find_element(By.LINK_TEXT,"Register").click()
time.sleep(2)
#or
# driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()
time.sleep(2)

#xpath locator
driver.find_element(By.XPATH, "//img[@alt='nopCommerce demo store']").click()
time.sleep(2)

#class name locator
prods_qty=driver.find_elements(By.CLASS_NAME,"item-box")
time.sleep(2)
print(len(prods_qty))

#tag name locator
links=driver.find_elements(By.TAG_NAME, "a")
print(len(links))

# driver.close()
driver.quit()