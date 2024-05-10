from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

windowID=driver.current_window_handle
print("Current window ID is :",windowID)
time.sleep(2)


driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
Window_Ids=driver.window_handles

#Approach 1)
parent_window=Window_Ids[0]
child_window=Window_Ids[1]
print("Parent window ID :",parent_window)
print("Child window ID :",child_window)

driver.switch_to.window(child_window)
print("Title of child window :",driver.title)
driver.switch_to.window(parent_window)
print("Title of parent window :",driver.title)

time.sleep(3)


#Approach 2)
for winId in Window_Ids:
    driver.switch_to.window(winId)
    print("Window title is :",driver.title)


#Want to claosed specific browser window
for winId in Window_Ids:
    driver.switch_to.window(winId)
    if driver.title == "OrangeHRM":
        driver.close()


time.sleep(3)
driver.quit()