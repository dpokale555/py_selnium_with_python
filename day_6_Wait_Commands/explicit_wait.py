from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# mywait=WebDriverWait(driver,10)   #explicit wait declaration #basic syntax
mywait=WebDriverWait(driver,10,poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                            ElementNotVisibleException,
                                                            ElementNotSelectableException,
                                                            Exception])

driver.get("https://www.google.com/")
driver.maximize_window()
search_box=driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
search_box.send_keys("Selenium")
search_box.submit()

searchlink=mywait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']")))
searchlink.click()

driver.quit()


