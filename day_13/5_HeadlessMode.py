import os
from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.support.select import Select
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver = webdriver.Chrome(options=ops)
    return driver

def headless_edge():
    from selenium.webdriver.support.select import Select
    ops=webdriver.EdgeOptions()
    ops.headless=True
    driver = webdriver.Chrome(options=ops)
    return driver

def headless_firefox():
    from selenium.webdriver.support.select import Select
    ops=webdriver.FirefoxOptions()
    ops.headless=True
    driver = webdriver.Chrome(options=ops)
    return driver

# driver=headless_chrome()
driver=headless_edge()
# driver=headless_firefox()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title)
print(driver.current_url)
driver.quit()