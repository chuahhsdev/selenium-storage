from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import math

from timeit import default_timer as timer

driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
driver.get("https://demoqa.com/automation-practice-form")

print("Selenium start! Now starting time.")
start = timer()

# Functions!
def round_time(end, start):
  final_time = end - start
  final_time_rounded = math.floor(final_time * 100)/100.0
  return final_time_rounded
  

#Get all the fields for this form
firstName_field = driver.find_element(By.ID, "firstName") 
lastName_field = driver.find_element(By.ID, "lastName")
userEmail_field = driver.find_element(By.ID, "userEmail")

gender_male_radio = driver.find_element(By.ID, "gender-radio-1")
gender_female_radio = driver.find_element(By.ID, "gender-radio-2")
gender_other_radio = driver.find_element(By.ID, "gender-radio-3")

userNumber_field = driver.find_element(By.ID, "userNumber")
dateOfBirthInput_field = driver.find_element(By.ID, "dateOfBirthInput")
subjectsContainer_field = driver.find_element(By.ID, "subjectsContainer")

uploadPicture_field = driver.find_element(By.ID, "uploadPicture")

currentAddress_field = driver.find_element(By.ID, "currentAddress")
state_field = driver.find_element(By.ID, "state")
city_field = driver.find_element(By.ID, "city")

print("aa");

#End the current log time.
end = timer()
f_time = round_time(end, start)
print("Total time: "+ str(f_time)+"s") # Time in seconds, e.g. 5.38091952400282

driver.quit() # closes lol