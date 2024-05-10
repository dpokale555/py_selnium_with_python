from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
download_location=os.getcwd()

def chrome_setup():
    #To download the file at desire location
    # preferences={"download.default.directory":"C:\Users\dhananjay.pokale\Desktop\AWS_practice\Python_Learning\Selnium123\day_12"}
    preferences = {"download.default.directory": download_location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)

    My_Driver = webdriver.Chrome(options=ops)
    return My_Driver

def firefox_setup():
    preferences = {"download.default.directory": download_location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    My_Driver = webdriver.Firefox(options=ops)
    return My_Driver

def edge_setup():
    preferences = {"download.default.directory": download_location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    My_Driver = webdriver.Edge(options=ops)
    return My_Driver


# driver=chrome_setup()
# driver=firefox_setup()
driver=edge_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
time.sleep(3)
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
time.sleep(10)
driver.quit()