from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

driver.find_element(By.XPATH,"//li[1]//a[1]//span[1]").click()

# driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
# driver.find_element(By.XPATH,"//ul[@class='oxd-dropdown-menu']//li").click()

total_rows=len(driver.find_elements(By.XPATH,"//div[@role='row']"))
print("Total Number of rows :",total_rows)


time.sleep(3)

