from selenium import webdriver
#webdriver is one of the component or module in selenium. To work with webdriver we have to import it from selenium
#for slowing the time process while execution

#we import regular expression to validate the user name and password
from selenium.webdriver.common.by import By
#to use locator we have to import By

driver= webdriver.Chrome()
driver.implicitly_wait(5)
#declaring the path of chrome driver.

driver.get("https://www.google.com/")
driver.find_element(By.XPATH,'//textarea[@class="gLFyf"]').send_keys("GitHub")
storage = driver.find_elements(By.CSS_SELECTOR,"ul.G43f7e li span")
print(len(storage))
for element in storage:
    if element.text == "github login":
        element.click()
        break

# print(len(temporary))
if driver.title =="github login - Google Search":
    print("testcase passed")
else:
    raise "failed"
driver.quit()