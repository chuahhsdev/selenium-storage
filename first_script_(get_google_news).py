from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
driver.get("https://news.google.com/home?hl=en-MY&gl=MY&ceid=MY:en")

headlines = driver.find_elements(By.CLASS_NAME, "gPFEn")  # Find all headlines
for headline in headlines[:5]:  # Print first 5 headlines
    print(headline.text)

time.sleep(10)  # Keep the browser open for 10 seconds

driver.quit() # closes lol