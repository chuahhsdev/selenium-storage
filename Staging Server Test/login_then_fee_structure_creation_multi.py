from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import sys
import time
import math

from timeit import default_timer as timer

def round_time(end, start):
  final_time = end - start
  final_time_rounded = math.floor(final_time * 100)/100.0
  return final_time_rounded
  

chrome_options = Options()
#chrome_options.add_argument('--log-level=3') #just to not show the tensorflow error thing, remove this if you want

# Set up WebDriver (Change path if necessary)
driver = webdriver.Chrome()

print("Selenium start! Now starting time.")
start = timer()

driver.get("")  # Replace with actual login URL
driver.maximize_window()
#time.sleep(3)  # Wait for the page to load
driver.implicitly_wait(3)  

# Step 1: Open the login page

# Step 2: Locate and fill in login details
username_field = driver.find_element(By.ID, "user_name")  # Adjust selector
password_field = driver.find_element(By.ID, "password")  # Adjust selector

username_field.send_keys("compliance2")
password_field.send_keys("Hello-123")

# Step 3: Click the login button
login_button = driver.find_element(By.ID, "btnLogin")  # Adjust selector
login_button.click()

# Step 4: Verify successful login
#time.sleep(3)  # Wait for page to load
driver.implicitly_wait(3)  

# What's XPath aaa
# This assumes that when the user logs in, they'll see the dashboard
element = driver.find_elements(By.XPATH, "//h3[text()='Latest Order']") #Relative XPath, Searches for elements anywhere in the document, making it more flexible.

# XPath Glossary
# Locate a Button by Text: //button[text()='Login']
# Find an Input Field by ID: //input[@id='username']

# Chained XPath Example
# WebElement form = driver.findElement(By.xpath("//form[@id='loginForm']"));
# WebElement usernameInput = form.findElement(By.xpath(".//input[@name='username']"));

check_login = False

for h3 in element: 
    if h3.text == "LATEST ORDER":
        check_login = True
        
if (check_login == False):
    print("Login failed!")
    driver.quit()
    
#hey hey yeah we got in

fee_structure_setting_button = driver.find_element(By.XPATH, "//a[@href='index.php?p=fee_structure_setting']")
driver.execute_script("arguments[0].scrollIntoView();", fee_structure_setting_button) # Scrolls into view so Selenium can click it

#How @ Works in XPath
#@attribute_name refers to an HTML attribute inside an element.
# In Selenium, @ is used in XPath to select attributes of an HTML element.

fee_structure_setting_button.click()

#time.sleep(2)  # Wait for page to load
driver.implicitly_wait(3)  

# =========== FEE STRUCTURE =========== 
# EDITING PLACE

#This one is creating multiple at once! Hooray!
fee_name = ["EDP - Half Day - 2025 Test", "EDP - Full Day - 2025 Test", 
"QF1 - Half Day - 2025 Test", "QF1 - Full Day - 2025 Test", 
"QF2 - Half Day - 2025 Test", "QF2 - Full Day - 2025 Test",
"QF3 - Half Day - 2025 Test", "QF3 - Full Day - 2025 Test"]
subject_var = ["EDP", "EDP", "QF1", "QF1", "QF2", "QF2", "QF3", "QF3"]
programme_package_var = ["Half Day", "Full Day", "Half Day", "Full Day", "Half Day", "Full Day", "Half Day", "Full Day"]

counter = 0 #counter to keep track of the other arrays in subject_var and programme_package_var

for fee_names in fee_name:
    #fee_name = "QF2 - Half Day - 2025 - Selenium"
    #subject_var = "QF2"
    #programme_package_var = "Half Day"

    fee_structure_name_field = driver.find_element(By.ID, "fees_structure")  # Adjust selector
    fee_structure_name_field.send_keys(fee_names)

    print("Now attempting to add new Fee Structure: "+fee_names)

    # Select stuff
    subject_dropdown = driver.find_element(By.ID, "subject")
    subject_select = Select(subject_dropdown)
    subject_select.select_by_visible_text(subject_var[counter])

    programme_package_dropdown = driver.find_element(By.ID, "programme_package")
    programme_package_select = Select(programme_package_dropdown)
    programme_package_select.select_by_visible_text(programme_package_var[counter])

    #scrolls to submit button
    submit_fee_structure_button = driver.find_element(By.CLASS_NAME, "uk-button-primary")
    remarks_field = driver.find_element(By.ID, "remarks")

    driver.execute_script("arguments[0].scrollIntoView();", remarks_field) # Scrolls into view so Selenium can click it
    #driver.execute_script("window.scrollBy(0, -500);")  # Scroll up 500 pixels

    time.sleep(2)  # Wait for page to load
    submit_fee_structure_button.click()
    time.sleep(1)  # Wait for page to load
    try:
        check_error = driver.find_element(By.XPATH, "//h2[text()='Fees structure name already exist']") # Checking Fee Structure Duplication Error
        print("Fee Structure name already exists, please edit the code")
        driver.quit()
    
        end = timer()
        f_time = round_time(end, start)
    
        print("Total time: "+ str(f_time)+"s") # Time in seconds, e.g. 5.38091952400282
        exit()
    except NoSuchElementException:
        print("Fee Structure Created ("+fee_names+")")
        pass
    
    counter = counter + 1
    #time.sleep(3)  # Wait for page to load
    driver.implicitly_wait(3)  

#End the current log time.
end = timer()
f_time = round_time(end, start)
print("Total time: "+ str(f_time)+"s") # Time in seconds, e.g. 5.38091952400282


# Step 5: Close browser
driver.quit()
