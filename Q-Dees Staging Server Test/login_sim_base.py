from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver (Change path if necessary)
driver = webdriver.Chrome()

#driver.get("")  # Replace with actual login URL
# Step 1: Open the login page
time.sleep(2)  # Wait for the page to load

# Step 2: Locate and fill in login details
username_field = driver.find_element(By.ID, "user_name")  # Adjust selector
password_field = driver.find_element(By.ID, "password")  # Adjust selector

username_field.send_keys("") #replace with actual username
password_field.send_keys("") #replace with actual password

# Step 3: Click the login button
login_button = driver.find_element(By.ID, "btnLogin")  # Adjust selector
login_button.click()

# Step 4: Verify successful login
time.sleep(5)  # Wait for page to load

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

# Step 5: Close browser
#driver.quit()