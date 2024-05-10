from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#############  find_element() : Always returns single weblelement

#Senario 1: Locator matching with the seingle weblement
element1=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
element1.send_keys("Apple MacBook Pro 13-inch")
element1.clear()

#Senario 2: Locator matching with the multiple weblements
element2=driver.find_element(By.XPATH,"//div[@class='footer']//a")
print("Always return the fist element :",element2.text)

#Senario 3: Locator matching with the no weblements then throw NoSuchElementException
# element3=driver.find_element(By.LINK_TEXT,"Log innnnnn")
# element3.click()


#############  find_elements() : Always returns multiple weblelement

#Senario 1: Locator matching with the seingle weblement
element4=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
print("Total length :",len(element4))
element4[0].send_keys("Apple MacBook Pro 13-inch")

#Senario 2: Locator matching with the multiple weblements
element5=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print("Total no of links in footer :",len(element5))
print("return the element by Index :",element5[0].text)

for ele in element5:
    print("-->",ele.text)

#Senario 3: Locator matching with the no weblements then throw NoSuchElementException
element6=driver.find_elements(By.LINK_TEXT,"Log innnnnn")
print("Total elements :",len(element6))


