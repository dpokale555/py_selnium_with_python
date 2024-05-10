import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
time.sleep(2)

#Note:" We need to install 'requests' package through file --> PackageInterpeter

all_links=driver.find_elements(By.TAG_NAME,'a')
print(len(all_links))
count=0
for link in all_links:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None

    if res.status_code>=400:
        print(url," is broken link")
        count+=1
    else:
        print(url," is valid link")

print("Total number of broken links :",count)
