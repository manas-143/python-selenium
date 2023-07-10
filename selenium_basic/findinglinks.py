from selenium import webdriver
#webdriver is one of the component or module in selenium. To work with webdriver we have to import it from selenium
#for slowing the time process while execution

#we import regular expression to validate the user name and password
from selenium.webdriver.common.by import By
#to use locator we have to import By

driver= webdriver.Chrome()
driver.implicitly_wait(5)
#declaring the path of chrome driver.

driver.get("https://www.amazon.com/")

store = driver.find_elements(By.TAG_NAME,"a")
print({i.text:i.get_attribute("href") for i in store if i.text !=""})

driver.quit()