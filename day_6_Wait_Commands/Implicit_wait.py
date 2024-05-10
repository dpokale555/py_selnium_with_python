from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.google.com/")
driver.maximize_window()
search_box=driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
search_box.send_keys("Selenium")
search_box.submit()


driver.find_element(By.XPATH,"//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']").click()




