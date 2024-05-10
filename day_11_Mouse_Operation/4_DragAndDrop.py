from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html#google_vignette")
driver.maximize_window()
driver.implicitly_wait(10)

time.sleep(3)
Source_Oslo=driver.find_element(By.XPATH,"//div[@id='box1']")
Source_StockHome=driver.find_element(By.XPATH,"//div[@id='box2']")
Source_Washington=driver.find_element(By.XPATH,"//div[@id='box3']")
Source_Copenhagen=driver.find_element(By.XPATH,"//div[@id='box4']")
Source_Seoul=driver.find_element(By.XPATH,"//div[@id='box5']")
Source_Rome=driver.find_element(By.XPATH,"//div[@id='box6']")
Source_Madrid=driver.find_element(By.XPATH,"//div[@id='box7']")

Target_Norway=driver.find_element(By.XPATH,"//div[@id='box101']")
Target_Sweden=driver.find_element(By.XPATH,"//div[@id='box102']")
Target_US=driver.find_element(By.XPATH,"//div[@id='box103']")
Target_Denmark=driver.find_element(By.XPATH,"//div[@id='box104']")
Target_South_Korea=driver.find_element(By.XPATH,"//div[@id='box105']")
Target_Italy=driver.find_element(By.XPATH,"//div[@id='box106']")
Target_Spain=driver.find_element(By.XPATH,"//div[@id='box107']")

act=ActionChains(driver)

act.drag_and_drop(Source_Oslo, Target_Norway).perform()
act.drag_and_drop(Source_StockHome, Target_Sweden).perform()
act.drag_and_drop(Source_Washington, Target_US).perform()
act.drag_and_drop(Source_Copenhagen, Target_Denmark).perform()
act.drag_and_drop(Source_Seoul, Target_South_Korea).perform()
act.drag_and_drop(Source_Rome, Target_Italy).perform()
act.drag_and_drop(Source_Madrid, Target_Spain).perform()

time.sleep(4)


