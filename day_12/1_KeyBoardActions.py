from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://text-compare.com/")
driver.maximize_window()
driver.implicitly_wait(10)

textbox1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
textbox2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

textbox1.send_keys("Hello! Welcome")

act=ActionChains(driver)

#Textbox1 ---> CTR+A   (Select the text)
# act.key_down(Keys.CONTROL)
# act.send_keys('a')
# act.key_up(Keys.CONTROL)
# act.perform()

# OR

act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

#Textbox1 ---> CTR+C   (Copy the text)
# act.key_down(Keys.CONTROL)
# act.send_keys('c')
# act.key_up(Keys.CONTROL)
# act.perform()

#OR
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#Move to the second text box by 'TAB' Key
act.send_keys(Keys.TAB).perform()

#Textbox2 ---> CTR+V   (Pase the text)
# act.key_down(Keys.CONTROL)
# act.send_keys("v")
# act.key_up(Keys.CONTROL)
# act.perform()

#OR
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(4)

driver.quit()