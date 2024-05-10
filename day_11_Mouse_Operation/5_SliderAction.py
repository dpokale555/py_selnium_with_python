from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
driver.implicitly_wait(10)

min_slider=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
max_slider=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")

print("Location of slider before moving :",min_slider.location)
print("Location of slider before moving :",max_slider.location)

act=ActionChains(driver)

act.drag_and_drop_by_offset(min_slider, 200,0).perform()
act.drag_and_drop_by_offset(max_slider, -100,0).perform()

print("Location of slider before moving :",min_slider.location)
print("Location of slider before moving :",max_slider.location)

time.sleep(3)