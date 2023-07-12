from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_con
import time
driver = webdriver.Chrome()
driver.get('https://app.hubspot.com/login')
driver.maximize_window()
wait = WebDriverWait(driver,10)
# email_id = wait.until(exp_con.presence_of_element_located((By.XPATH, "//input[@id='username']")))
# email_id.send_keys('Sid123@gmail.com')
# pas=driver.find_element(By.XPATH,"//input[@id='password']")
# pas.send_keys('1234567')
# lgbtn=driver.find_element(By.XPATH,"//button[@id='loginBtn']")
# lgbtn.click()
#Here WE give time only for email_id and after that we direclty used other web-element
#presence_of_element_located-Used to check whether the given element is located at that location or not and if present return address of that
#title_is and title_contains-Used for checking the title
if wait.until(exp_con.title_contains('Hub')):
    print(driver.title)

#visibility_of_element - It shows at given location element is visible or not and return address of element
# email_id=wait.until(exp_con.visibility_of_element_located((By.XPATH,"//input[@id='username']")))
# email_id.send_keys('sid123@gmail.com')
# email_id.send_keys('Sid123@gmail.com')
# pas=driver.find_element(By.XPATH,"//input[@id='password']")
# pas.send_keys('1234567')
# lgbtn=driver.find_element(By.XPATH,"//button[@id='loginBtn']")
# lgbtn.click()
# time.sleep(2)

#text_to_be_present_in_element- It return boolean value based on condition(if given text is available at the location return true else return false)
sign_in=wait.until(exp_con.text_to_be_present_in_element((By.XPATH,'//*[@class="signup-link"]/child::a'),'Sb'))
print(sign_in)

driver.close()

