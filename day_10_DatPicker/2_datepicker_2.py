from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from datetime import datetime

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(10)

date="20"
month="Jun"
year="2023"

driver.find_element(By.XPATH,"//input[@id='dob']").click()
all_month=driver.find_element(By.XPATH,"//select[@aria-label='Select month']")
drpmonth=Select(all_month)
drpmonth.select_by_visible_text(month)

yearlist = driver.find_elements(By.XPATH,"//select[@aria-label='Select year']/option")

for i in range(len(yearlist)+1):
    if yearlist[i].get_attribute('value')==year:
        yearlist[i].click()
        break

all_dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for dt in all_dates:
    if dt.text==date:
        dt.click()
        break

time.sleep(4)

driver.quit()
