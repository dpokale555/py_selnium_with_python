import time

import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Day_14_Data_Driven_testing2 import XLUtils
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.implicitly_wait(10)
driver.maximize_window()

file="C:\\Users\\dhananjay.pokale\\Desktop\\MyPersonal\\Python_DurgaSoft\\intrest_rate.xlsx"
rows=XLUtils.getRowCount(file,"Sheet11")

for r in (2,rows+1):
    price=XLUtils.readData(file,"Sheet11",r,1)
    ROI=XLUtils.readData(file,"Sheet11",r,2)
    per1 = XLUtils.readData(file, "Sheet11", r, 3)
    per2 = XLUtils.readData(file, "Sheet11",r,4)
    freq = XLUtils.readData(file, "Sheet11", r, 5)
    exp_value = XLUtils.readData(file, "Sheet11",r,6)

    #passing data to the application
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(price)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(ROI)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)

    period_drop=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    period_drop.select_by_visible_text(per2)

    freq_drop=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    freq_drop.select_by_visible_text(freq)

    driver.find_element(By.XPATH,"//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()

    act_value=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

#Validation
    if float(exp_value)==float(act_value):
        print("Test Case Pass")
        XLUtils.writeData(file,"Sheet11",r,8,"Passed")
        XLUtils.fileGreenColor(file,"Sheet11",r,8)
    else:
        print("Test Case Failed")
        XLUtils.writeData(file, "Sheet11", r, 8, "Failed")
        XLUtils.fileRedColor(file, "Sheet11", r, 8)

    driver.find_element(By.XPATH,"//img[@class='PL5']").click()
    time.sleep(2)






