from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#Prevent Stale Elements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

from timeit import default_timer as timer

driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
# Wait for the elements to be available
wait = WebDriverWait(driver, 10)

driver.get("https://demoqa.com/automation-practice-form")

# Variables to input
firstName_var = "Chuah"
lastName_var = "Hiap Seng"
userEmail_var = "chuahhs@outlook.com"

gender_var = "Male"

userNumber_var = "0122028955"

dateOfBirthInput_var_month = "August"
dateOfBirthInput_var_year = "1990"
dateOfBirthInput_var_day = "24"

subjectsContainer_var = "Computer Science"

hobbies_checkbox_var_1 = "N"
hobbies_checkbox_var_2 = "Y"
hobbies_checkbox_var_3 = "Y"

currentAddress_var = "Bandar Utama Damansara 47800"
state_var = "Rajasthan"
city_var = "Jaipur"

# Functions!
def round_time(end, start):
  final_time = end - start
  final_time_rounded = math.floor(final_time * 100)/100.0
  return final_time_rounded
  
# =========
print("Selenium start! Now starting time.")
start = timer()

#Get all the fields for this form
firstName_field = driver.find_element(By.ID, "firstName") 
lastName_field = driver.find_element(By.ID, "lastName")
userEmail_field = driver.find_element(By.ID, "userEmail")

#gender_male_radio = driver.find_element(By.ID, "gender-radio-1")
#gender_female_radio = driver.find_element(By.ID, "gender-radio-2")
#gender_other_radio = driver.find_element(By.ID, "gender-radio-3")

gender_male_radio = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
gender_female_radio = driver.find_element(By.XPATH, "//label[@for='gender-radio-2']")
gender_other_radio = driver.find_element(By.XPATH, "//label[@for='gender-radio-3']")

userNumber_field = driver.find_element(By.ID, "userNumber")
dateOfBirthInput_field = driver.find_element(By.ID, "dateOfBirthInput")
subjectsInput_field = driver.find_element(By.ID, "subjectsInput")

uploadPicture_field = driver.find_element(By.ID, "uploadPicture")

currentAddress_field = driver.find_element(By.ID, "currentAddress")
state_field = driver.find_element(By.ID, "state")
city_field = driver.find_element(By.ID, "city")

# Begin send keys
driver.execute_script("arguments[0].scrollIntoView();", firstName_field) # Scrolls into view so Selenium can click it

firstName_field.send_keys(firstName_var)
lastName_field.send_keys(lastName_var)
userEmail_field.send_keys(userEmail_var)

if gender_var == "Male":
    gender_male_radio.click()
elif  gender_var == "Female":
    gender_female_radio.click()
else:
    gender_other_radio.click()

userNumber_field.send_keys(userNumber_var)

# DoB Section
dateOfBirthInput_field.click()

time.sleep(2)  # Wait up to 10 seconds

#month_field = Select(driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']"))
month_field = driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']")
year_field = driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']")
#year_field = Select(driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']"))
#day_field = driver.find_element(By.XPATH, "//div[@class='react-datepicker__day']")

driver.execute_script("arguments[0].scrollIntoView();", month_field) # Scrolls into view so Selenium can click it

month_field_select = Select(month_field)
year_field_select = Select(year_field)

time.sleep(1)  # Wait up to 10 seconds

# select by visible text
month_field_select.select_by_visible_text(dateOfBirthInput_var_month)
year_field_select.select_by_visible_text(dateOfBirthInput_var_year)
time.sleep(2)  # Wait up to 10 seconds

# Wait for the date to become visible and clickable
day_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'react-datepicker__day--024')]"))
)
day_element.click()
time.sleep(3)  # Wait up to 10 seconds
#for element in driver.find_elements_by_class_name('react-datepicker__day'):
#for element in driver.find_elements(By.CLASS_NAME, "react-datepicker__day"):
#    print(element.text)
#    if element.text == dateOfBirthInput_var_day:
#        # Re-locate the element just before clicking to avoid stale element issues
#        date_element = driver.find_element(By.XPATH, "//*[contains(@class, 'react-datepicker__day--024')]")
#        date_element.click()  # If you need to click it
#        break  # Exit loop after clicking

# Subjects
driver.execute_script("arguments[0].scrollIntoView();", subjectsInput_field) # Scrolls into view
print("a")
subjectsInput_field.click();

subjectsInput_field.send_keys("Computer Science")
print("b")
subjectsInput_field.send_keys(Keys.ENTER)  # Press Enter
# State and City
state_field = driver.find_element(By.ID, "state")
state_field.click()
option = driver.find_element(By.XPATH, f"//div[contains(text(), '{state_var}')]")
driver.execute_script("arguments[0].click();", option)
time.sleep(2)

#city_field.selectByVisibleText(city_var);
city_field = driver.find_element(By.ID, "city")
print("fff")
city_field.click()
print("sfas")
time.sleep(1)
# Type it instead
city_field.send_keys("Jaipur")
print("asd")
time.sleep(2)
city_field.send_keys(Keys.ENTER)  # Delete selected text
#option = driver.find_element(By.XPATH, f"//div[contains(text(), '{city_var}')]")


time.sleep(10)

#End the current log time.
end = timer()
f_time = round_time(end, start)
print("Total time: "+ str(f_time)+"s") # Time in seconds, e.g. 5.38091952400282

driver.quit() # closes lol