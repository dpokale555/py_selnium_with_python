from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()
time.sleep(2)

#CSS_Selector Combination. In all combinations Tag name is an optional
#1) Tag and ID  --> Syntax: tagname#ValueOfID
driver.find_element(By.CSS_SELECTOR,"input#search_query_top").send_keys("T-shirts")
time.sleep(2)

#2) Tag and Class --> Syntax: tagname#ValueOfClass
driver.find_element(By.CSS_SELECTOR, "button.btn").click()
time.sleep(2)

driver.find_element(By.XPATH, "//a[@title='Log in to your customer account']").click()

#3) Tag and Attribute --> Syntax: tagname[attribute=value]
driver.find_element(By.CSS_SELECTOR, "input[id=email]").send_keys("abcd@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[data-validate=isPasswd]").send_keys("Password")
time.sleep(2)

#4) Tag, Class and Attributes--> Syntax: tagname.ValueOfClass[attribute=value]
driver.find_element(By.CSS_SELECTOR, "input.is_required[data-validate=isEmail]").send_keys("xyz@gmail.com")
time.sleep(3)
