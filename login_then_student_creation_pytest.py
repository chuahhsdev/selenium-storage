from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

from config import login_link #Imports Login URL. Please replace with Actual Test Server

import pytest 

import sys
import time
import math

import random #randomize selection

from timeit import default_timer as timer

from faker import Faker

def round_time(end, start):
  final_time = end - start
  final_time_rounded = math.floor(final_time * 100)/100.0
  return final_time_rounded

chrome_options = Options()
#chrome_options.add_argument('--log-level=3') #just to not show the tensorflow error thing, remove this if you want

# Command to run: pytest login_then_student_creation_pytest.py
@pytest.fixture
def setup_browser():
    # Set up WebDriver (Change path if necessary)
    driver = webdriver.Chrome()

    driver.get(login_link)  # Replace with actual login URL
    driver.maximize_window()
    #time.sleep(3)  # Wait for the page to load
    driver.implicitly_wait(3) 
    #Time to login
    username_field = driver.find_element(By.ID, "user_name")  # Adjust selector
    password_field = driver.find_element(By.ID, "password")  # Adjust selector

    username_field.send_keys("testing z")
    password_field.send_keys("abc123$")
    
    login_button = driver.find_element(By.ID, "btnLogin")  # Adjust selector
    login_button.click()
    
     # Step 4: Verify successful login
    #time.sleep(3)  # Wait for page to load
    driver.implicitly_wait(3)  
    
    element = driver.find_elements(By.XPATH, "//h3[text()='Latest Order']") #Relative XPath, Searches for elements anywhere in the document, making it more flexible.

    check_login = False

    for h3 in element: 
        if h3.text == "LATEST ORDER":
            check_login = True
            
    if (check_login == False):
        print("Login failed!")
        driver.quit()
        
    #hey hey yeah we got in
    fee_structure_setting_button = driver.find_element(By.XPATH, "//a[@href='index.php?p=student']")
    #driver.execute_script("arguments[0].scrollIntoView();", fee_structure_setting_button) # Scrolls into view so Selenium can click it
    fee_structure_setting_button.click()
    
    driver.implicitly_wait(3)
    student_registration_button = driver.find_element(By.XPATH, "//a[@href='index.php?p=student_reg']")
    student_registration_button.click()
    
    #Testing time!
    yield driver
    
    #All done, time to quit
    driver.quit()
    

# Step 1: Open the login page

# ========== TEST CASES ==========
def test_fill_form_valid_data(setup_browser):
    driver = setup_browser  # Assign the fixture return value to driver
    f = Faker() #Fake name! :D
    
    print("Selenium start! Now starting time.")
    start = timer()
    
    driver.implicitly_wait(3) #wait for page to load
    
    name_field = driver.find_element(By.ID, "name")  # Adjust selector
    name_field.send_keys(f.name())
    
    # Start Date at Center
    # ########
    date_input = driver.find_element(By.ID, "start_date_at_centre")
    date_input.click()
    
    # Find today's date in the calendar, just make it easier lol
    today_element = driver.find_element(By.CLASS_NAME, "uk-active")
    today_element.click()
    
    driver.find_element(By.ID, "form_serial_no").send_keys("123456789")
    
    #Parent Contact
    parent_field = driver.find_element(By.ID, "primary-contact1")
    parent_field.click()
    time.sleep(1)
    #Begin inputting everything!
    form = driver.find_element(By.ID, "frmSaveContact")
    
    contact_type_dropdown = form.find_element(By.NAME, "contact_type[]")
    contact_type_select = Select(contact_type_dropdown)
    contact_type_select.select_by_visible_text("Father")
    
    driver.find_element(By.NAME, "full_name[]").send_keys(f.name())
    
    ic_string = "9" #create a random IC
    countericloop = 0
    
    while countericloop < 11:
        ic_string += str(random.randint(0, 9))
        countericloop += 1
 
    driver.find_element(By.NAME, "nric[]").send_keys(str(ic_string))
    
    driver.find_element(By.NAME, "email[]").send_keys("seleniumtest@gmail.com")
    driver.find_element(By.NAME, "mobile[]").send_keys("128844334")
    
    occupation_dropdown = form.find_element(By.NAME, "occupation[]")
    occupation_select = Select(occupation_dropdown)
    occupation_select.select_by_visible_text("Manufacturing")
    
    education_level_dropdown = form.find_element(By.NAME, "education_level[]")
    education_level = Select(education_level_dropdown)
    education_level.select_by_index(1)
    #education_level.select_by_visible_text("Bachelors Degree")

    can_pick_dropdown = form.find_element(By.NAME, "can_pick_up[]")
    can_pick = Select(can_pick_dropdown)
    can_pick.select_by_index(1)
    
    form.find_element(By.NAME, "vehicle_no[]").send_keys("WMP 4295")

    form.find_element(By.NAME, "remarks[]").send_keys("Selenium Input")
    submit_button = form.find_element(By.XPATH, ".//button[@type='submit']")
    submit_button.click()
    time.sleep(1)
    #back to the main form we go
    driver.find_element(By.ID, "nric_no").send_keys("989531235823")
    
    dob_day_dropdown = driver.find_element(By.ID, "dob_day")
    dob_day_select = Select(dob_day_dropdown)
    dob_day_select.select_by_visible_text("24")
    
    dob_month_dropdown = driver.find_element(By.ID, "dob_month")
    dob_month_select = Select(dob_month_dropdown)
    dob_month_select.select_by_visible_text("08")
    
    dob_year_dropdown = driver.find_element(By.ID, "dob_year")
    dob_year_select = Select(dob_year_dropdown)
    dob_year_select.select_by_visible_text("1990")
    
    driver.find_element(By.ID, "birth_cert_no").send_keys("987654321")
    
    gender_dropdown = driver.find_element(By.ID, "gender")
    gender_select = Select(gender_dropdown)
    gender_select.select_by_visible_text("Male")
    driver.execute_script("arguments[0].scrollIntoView();", gender_dropdown) # Scrolls into view so Selenium can click it
    driver.find_element(By.ID, "add1").send_keys("No. 6-4,")
    driver.find_element(By.NAME, "add2").send_keys("Level 4,")
    driver.find_element(By.NAME, "add3").send_keys("Jalan SS6/6 Kelana Jaya,")
    driver.find_element(By.NAME, "add4").send_keys("47301 Petaling Jaya, Selangor")
    
    #Country
    country_dropdown = driver.find_element(By.ID, "country")
    country_select = Select(country_dropdown)
    country_options = country_select.options
    country_options = country_options[1:] #Remove the Select from the Race (First option)
    # Randomly select an option
    country_option = random.choice(country_options)
    country_option.click() #Select changed how this works instead of visible text LOL
    
    #State
    state_dropdown = driver.find_element(By.ID, "state")
    state_select = Select(state_dropdown)
    state_options = state_select.options
    state_options = state_options[1:] #Remove the Select from the Race (First option)
    # Randomly select an option
    state_option = random.choice(state_options)
    state_option.click()
    
    #Race
    race_dropdown = driver.find_element(By.ID, "race")
    driver.execute_script("arguments[0].scrollIntoView();", race_dropdown) # Scrolls into view so Selenium can click it
    race_select = Select(race_dropdown)
    # gender_select.select_by_visible_text("Male")
    race_options = race_select.options
    race_options = race_options[1:] #Remove the Select from the Race (First option)
    # Randomly select an option
    random_option = random.choice(race_options)
    random_option.click()
    
    #Nationality
    nationality_dropdown = driver.find_element(By.ID, "nationality")
    driver.execute_script("arguments[0].scrollIntoView();", nationality_dropdown) # Scrolls into view so Selenium can click it
    nationality_select = Select(nationality_dropdown)
    # gender_select.select_by_visible_text("Male")
    nationality_options = nationality_select.options
    nationality_options = nationality_options[1:] #Remove the Select from the Race (First option)
    # Randomly select an option
    random_option = random.choice(nationality_options)
    random_option.click()
    
    #Religion
    religion_dropdown = driver.find_element(By.ID, "religion")
    driver.execute_script("arguments[0].scrollIntoView();", religion_dropdown) # Scrolls into view so Selenium can click it
    religion_select = Select(religion_dropdown)
    # gender_select.select_by_visible_text("Male")
    religion_options = religion_select.options
    religion_options = religion_options[1:] #Remove the Select from the Race (First option)
    # Randomly select an option
    random_option = random.choice(religion_options)
    random_option.click()
    
    #Medical Condition
    driver.find_element(By.ID, "health_problem").send_keys("NONE")
    
    # Allergies
    driver.find_element(By.ID, "allergies").send_keys("NONE")
    
    # Allergies
    driver.find_element(By.ID, "remarks").send_keys("NONE")
    
    #Accept checkboxes
    accept_photo_dropdown = driver.find_element(By.ID, "accept_photo")
    accept_photo_dropdown.click()
    
    accept_terms_dropdown = driver.find_element(By.ID, "accept_terms")
    accept_terms_dropdown.click()
    
    #signature, copy and pasted and edited woops
    signature_canvas = driver.find_element(By.ID, "signature-container")
    signature_canvas.click()
    
    js_script = """
    var canvas = document.getElementById('signature-container').getElementsByTagName('canvas')[0];
    var context = canvas.getContext('2d');
    context.moveTo(10, 10);
    context.lineTo(100, 100);
    context.stroke();
    """
    driver.execute_script(js_script)
    
    #submit time!
    submit_btn = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView();", submit_btn) # Scrolls into view so Selenium can click it
    submit_btn.click()
    
    #load it
    driver.implicitly_wait(5) #wait for page to load
    #time.sleep(1)
    element = driver.find_element(By.CLASS_NAME, "uk-notify-message")
    if element.text != "Student registered successfully":
         pytest.fail(element.text)
    else:
        print(element.text)

    time.sleep(3)

    # #########################3
    #End the current log time.
    end = timer()
    f_time = round_time(end, start)
    print("Total time: "+ str(f_time)+"s") # Time in seconds, e.g. 5.38091952400282