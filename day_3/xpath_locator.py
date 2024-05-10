from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()

#XPATH with OR/AND
# driver.find_element(By.XPATH,"//input[@id='search_qrtff' or @name='search_query' ]").send_keys("T-Shirts")
# driver.find_element(By.XPATH,"//button[@name='submit_search' and @type='submit']").click()

#XPATH with contains and start-with
driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("T-Shirts")
driver.find_element(By.XPATH,"//button[start-with(@name,'submit_')]").click()