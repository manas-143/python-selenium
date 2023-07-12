import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_time
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("https://www.canva.com/")
driver.maximize_window()
wait=WebDriverWait(driver,10)
Business=driver.find_element(By.XPATH,"//span[@class='CMROvw' and text()='Design spotlight']")
action=ActionChains(driver)
action.move_to_element(Business).perform()
marketing=driver.find_element(By.XPATH,"//div[@class='ZU4_lw CP1jQw' and text()='Docs']")
marketing.click()
time.sleep(2)
driver.close()
"//div[@class='ZU4_lw CP1jQw' and text()='Brochures']"
