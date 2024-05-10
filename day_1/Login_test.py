from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
# driver=webdriver.Firefox()
# driver=webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
driver.find_element(By.NAME, 'username').send_keys("Admin")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)

act_title=driver.title
exp_title="OrangeHRM"

if act_title==exp_title:
    print("Login test Pass")
else:
    print("Login test failed")

driver.close()
