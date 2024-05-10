from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from datetime import datetime

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame(0)

#Approach 1:
# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("05/12/2024")
# time.sleep(3)
# driver.find_element(By.XPATH,"//input[@id='datepicker']").clear()
# time.sleep(3)

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
#Approcah 2:
date="10"
month="April"
year="2023"
input_date_obj = datetime.strptime("{} {} {}".format(date, month, year), "%d %B %Y")
current_date = datetime.now()

if input_date_obj>current_date:
    while True:
        act_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
        act_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
        if act_month == month and act_year == year:
            break
        else:
            driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

    all_dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']/table/tbody/tr/td/a")
    for dt in all_dates:
        if dt.text == date:
            dt.click()
            break

elif input_date_obj<current_date:
    while True:
        act_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
        act_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
        if act_month==month and act_year==year:
            break
        else:
            driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

    all_dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']/table/tbody/tr/td/a")
    for dt in all_dates:
        if dt.text==date:
            dt.click()
            break
else:
    all_dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']/table/tbody/tr/td/a")
    for dt in all_dates:
        if dt.text==date:
            dt.click()
            break

time.sleep(3)










