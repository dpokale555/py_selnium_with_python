from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

countriesList=driver.find_elements(By.XPATH,"//li[@class='select2-results__option']")
print(len(countriesList))

for cuntry in countriesList:
    if cuntry.text=="Honduras":
        print(cuntry.text)
        cuntry.click()
        time.sleep(3)
        break


