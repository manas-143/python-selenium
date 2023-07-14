import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
driver.get('https://www.facebook.com/')
driver.maximize_window()
wait=WebDriverWait(driver,20)
#Checking Create New Account Working Properly Or Not
create_new_acc=driver.find_element(By.XPATH,"//*[@class='_6ltg']/child::a")
create_new_acc.click()
time.sleep(5)
first_name=wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='_5dbb']/child::input")))
first_name.send_keys('Sid')
time.sleep(2)
surname=wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@name='lastname']")))
time.sleep(2)
surname.send_keys("Pandey")
email_phn=wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@name='reg_email__']")))
time.sleep(2)
email_phn.send_keys('9898989898')
time.sleep(2)
pwrd=wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//input[@id="password_step_input"]')))
pwrd.send_keys('123456789')
time.sleep(2)
day=wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//select[@id='day']")))
time.sleep(2)
select=Select(day)
dayopt=select.options
#Checking For All Day Are Clickable Or Not
days=[str(i) for i in range(1,35)]
try:
    for day in days:
        for d in dayopt:
            if day==d.text:
                d.click()
                break
        else:
            print(f'Given Day Value is Out of DropDown List {day}')
except Exception as msg:
    print(msg)
#
# #Checking For All Months are Clickable Or Not
month=wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//select[@id='month']")))
select=Select(month)
monthopt=select.options
months_for_test=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec','March']

try:
    for month in months_for_test:
        for m in monthopt:
            if month==m.text:
                m.click()
                time.sleep(1)
                break
        else:
            print(f'Given Month = {month} not in DropDown_List')
except ValueError:
    print(msg1)
# #
# #Checking Year DropDown Is Working Properly Or Not
year=wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//select[@id='year']")))
select=Select(year)
year_opt=select.options
years_for_testing=[str(y) for y in range(1900,2025)]
try:
    for year in years_for_testing:
        for y in year_opt:
            if year==y.text:
                y.click()
                # time.sleep(1)
                break
        else:
            print(f'Given Year is Not Present in DropDown_List {year}')
except Exception as msg:
    print(msg)
#
# # Checking For Radio Button
base_path="//span[@class='_5k_3']/child::span"
try:
    for i in range(1,4):
        rb = driver.find_element(By.XPATH, base_path + '[' + str(i) + ']')
        rb.click()
        if rb.is_selected():
            raise Exception('Radio Button Is Not Working Properly : ')
        # time.sleep(2)
    print('All Radio Buttons Working Properly')
except Exception as msg:
    print(msg)
#
# #Checking All Links Are Working Or Not
def checking_link(link):
    link_ele=driver.find_element(By.XPATH,link)
    link_ele.click()
    time.sleep(5)
    driver.close()

all_links=driver.find_elements(By.XPATH,"//*[@class='_8ien']/descendant::a")
print(len(all_links))
enabled_link=[]
for i in all_links:
    if i.is_enabled():
        enabled_link.append(i.get_attribute('href'))
print(len(enabled_link))
base_link="//*[@class='_8ien']/descendant::a"
all_active_link_path=[]
#
#
# #Checking all Link are working are not
Date_of_birth_link=checking_link("//*[@class='_8ien']/descendant::a[1]")
Gender=checking_link("//*[@class='_8ien']/descendant::a[3]")
learn_more=checking_link("//*[@class='_8ien']/descendant::a[4]")
Terms=checking_link("//*[@class='_8ien']/descendant::a[5]")
Privacy_Policy=checking_link("//*[@class='_8ien']/descendant::a[6]")
Cookies_Policy=checking_link("//*[@class='_8ien']/descendant::a[7]")


# #SingnUp Button  Testing
sign_up=driver.find_element(By.XPATH,"//button[@id='u_2_s_nS']")
time.sleep(5)
sign_up.click()


time.sleep(2)
driver.close()


#Full SignUp Testing
def Facbook_full_signup(first_name,last_name,em_pn,pwrd):
    try:
        driver.find_element(By.XPATH, "//*[@class='_6ltg']/child::a").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@class='_5dbb']/child::input").send_keys(first_name)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys(last_name)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='reg_email__']").send_keys(em_pn)
        time.sleep(2)
        driver.find_element(By.XPATH, '//input[@id="password_step_input"]').send_keys(pwrd)
        time.sleep(2)
        day = driver.find_element(By.XPATH, "//select[@id='day']")
        select_day = Select(day)
        select_day.options[2].click()
        time.sleep(2)

        month=driver.find_element(By.XPATH,"//select[@id='month']")
        select_month=Select(month)
        select_month.options[2].click()
        time.sleep(2)
        year=driver.find_element(By.XPATH,"//select[@id='year']")
        select_year=Select(year)
        select_year.options[45].click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//span[@class='_5k_3']/child::span[1]").click()
        time.sleep(2)
        sign_up=wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@class='_1lch']/child::button"))).click()
        sign_up.click()
        time.sleep(10)
    except Exception as msg:
        print(msg)
    else:
        #If First_Name Box is Not Following The Rule But Sign Up Button Taking Record It is a bug
        if not re.search('^[A-Z][a-z]+',first_name):
            print('Name Module Not Working Properly')
        # If Last Name is Not Following The Rule But Sign Up Button Taking Record It is a bug
        if not re.search('^[A-Z][a-z]+',first_name):
            print('Name Module Not Working Properly')
        # If Phone Number is Not Following The Rule But Sign Up Button Taking Record It is a bug
        if not re.search('^[789]\d{9}',em_pn):
            print('Email or Phone Module is Not Working Properly : ')
        # If Password is Not Following The Rule But Sign Up Button Taking Record It is a bug
        if len(pwrd)<=8:
            print('Password Module Not Working Properly')
        else:
            print('All Functionality is Working Fine ')
Facbook_full_signup('Saurav','Mehta','7992299039','@@@@@1234')


