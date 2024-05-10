import os

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(10)

#Method 1:
# driver.save_screenshot("C:\\Users\\dhananjay.pokale\\Desktop\\AWS_practice\\Python_Learning\\Selnium123\\day_13\\Homepage.png")

#Method 2:
# driver.save_screenshot(os.getcwd()+"\\homepagesnap.png")

#Method 3:
# driver.get_screenshot_as_file(os.getcwd()+"\\homepagefile.png")

#Method 4 and 5: using this method can store the screenshot in binarry format
# driver.get_screenshot_as_png(os.getcwd()+"\\homepagebin.png")
# driver.get_screenshot_as_base64(os.getcwd()+"\\homepagebinary.png")

driver.quit()