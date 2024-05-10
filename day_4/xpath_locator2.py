from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#Self
txt_self=driver.find_element(By.XPATH,"//a[normalize-space()='Inox Wind Ltd.']/self::a").text
print(txt_self)

#parent
txt_parent=driver.find_element(By.XPATH,"//a[normalize-space()='Inox Wind Ltd.']/parent::td").text
print(txt_parent)

#child
txt_child=driver.find_element(By.XPATH,"//a[normalize-space()='Inox Wind Ltd.']/ancestor::tr/child::td").text
print(txt_child)

#childs count
childs=driver.find_elements(By.XPATH,"//a[normalize-space()='Inox Wind Ltd.']/ancestor::tr/child::td")
print(len(childs))

#Ancestor
txt_ancestor=driver.find_element(By.XPATH,"//a[normalize-space()='Inox Wind Ltd.']/ancestor::tr").text
print(txt_ancestor)

#Descendant
descendants=driver.find_elements(By.XPATH,"//a[normalize-space()='Inox Wind Ltd.']/ancestor::tr/descendant::*")
print(len(descendants))

#Following
follwoings=driver.find_elements(By.XPATH,"//a[normalize-space()='Inox Wind Ltd.']/ancestor::tr/following::*")
print(len(follwoings))

#Following siblings
follwoing_siblings=driver.find_elements(By.XPATH,"//a[normalize-space()='Inox Wind Ltd.']/ancestor::tr/following-sibling::*")
print(len(follwoing_siblings))


#Preceding
precedings=driver.find_elements(By.XPATH,"//a[normalize-space()='Inox Wind Ltd.']/ancestor::tr/preceding::*")
print(len(precedings))

#Preceding siblings
preceding_siblings=driver.find_elements(By.XPATH,"//a[normalize-space()='Inox Wind Ltd.']/ancestor::tr/preceding-sibling::*")
print(len(preceding_siblings))



driver.close()

