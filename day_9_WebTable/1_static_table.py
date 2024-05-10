from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1) Count numbers of rows and columns
Total_rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
Total_columns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/th"))
print("Total numbers of rows :",Total_rows)
print("Total numbers of column :",Total_columns)

#2) read specific row and column data
#Approvcah 1)
print(driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[6]/td[2]").text)

#3) Read all the columns and rows data and ignore the haeder data
for i in range(2,Total_rows+1):
    for j in range(1,Total_columns+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(i)+"]/td["+str(j)+"]").text
        print(data,end='                ')
    print()

#4) Read the data based on the conditions
for r in range(2,Total_rows+1):
    auther_name=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if auther_name=="Mukesh":
        book_name=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        book_price = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[4]").text
        print(book_name,"  :  ",auther_name,"  :  ",book_price)

