from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1) Select the specific checkbox
driver.find_element(By.XPATH,"//input[@id='monday']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='monday']").click()

#2) Select all the checkboxes
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print("Total number of checkboxes :",len(checkboxes))

#Approach 1:
for i in range(len(checkboxes)):
    checkboxes[i].click()

print("All check boxes are checked")
time.sleep(2)

#Approach 2:
for chkbox1 in checkboxes:
    chkbox1.click()

print("All checkboxes uncheck")
time.sleep(2)

#3) Select multiple desired checkboxe
for chkbox in checkboxes:
    weekname=chkbox.get_attribute('id')
    if weekname=='tuesday' or weekname=='wednesday':
        chkbox.click()

print("two checkboxes check")
time.sleep(2)

#4) Select last two checkboxe
for i in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()

print("last two checkboxes check")
time.sleep(2)

#5) First last two checkboxe
for i in range(len(checkboxes)):
    if i<2:
        checkboxes[i].click()

print("first two checkboxes check")
time.sleep(2)

#6) Uncheck all the checkboxes which are checked
for chkbx in checkboxes:
    if chkbx.is_selected():
        chkbx.click()

print("All check boxes are unchecked")
time.sleep(3)

