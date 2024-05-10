from selenium import webdriver
from selenium.webdriver import ActionChains
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
time.sleep(3)

admin=driver.find_element(By.XPATH,"//li[1]//a[1]//span[1]")
user_mang=driver.find_element(By.XPATH,"//span[normalize-space()='User Management']")
user=driver.find_element(By.XPATH,"//a[@role='menuitem']")

act=ActionChains()

act.move_to_element(admin).move_to_element(user_mang).move_to_element(user).click()
time.sleep(3)

driver.quit()