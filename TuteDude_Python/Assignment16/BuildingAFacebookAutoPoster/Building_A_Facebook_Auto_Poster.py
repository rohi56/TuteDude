
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import time

# Setup Firefox driver
service = Service('C:/automationdrivers/firefox/geckodriver.exe')
driver = webdriver.Firefox(service=service)

# Open Facebook
driver.get("https://www.facebook.com/")
driver.maximize_window()

time.sleep(5)  # Wait for the page to load

emailelement = driver.find_element(By.XPATH, './/*[@id="email"]')
emailelement.send_keys('USERID_HERE')

time.sleep(5)
passelement = driver.find_element(By.XPATH, './/*[@id="pass"]')
passelement.send_keys('Password_Here')


# Click the login button
login_btn = driver.find_element(By.XPATH, './/*[@name="login"]')
login_btn.click()
time.sleep(10)  # Wait for login to complete

# Click the Home tab after login
try:
    home_btn = driver.find_element(By.XPATH, "//a[@aria-label='Home']")
    home_btn.click()
    print("Clicked Home tab.")
    time.sleep(5)
except Exception as e:
    print("Home tab not found or could not be clicked:", e)



# Step 1: Click the 'What's on your mind, Rohit?' span to open the dialog
try:
    open_dialog = driver.find_element(By.XPATH, "//span[contains(text(), \"What's on your mind, Rohit?\")]")
    open_dialog.click()
    time.sleep(2)

    # Step 2: Interact with the post input and post button
    post_input = driver.find_element(By.XPATH, "//div[@role='textbox']")
    post_input.click()
    time.sleep(2)
    # Clear any pre-filled text and send the full message character by character
    from selenium.webdriver.common.keys import Keys
    post_input.send_keys(Keys.CONTROL + 'a')
    post_input.send_keys(Keys.BACKSPACE)
    for char in 'Hi there, Good Morning':
        post_input.send_keys(char)
        time.sleep(0.05)
    time.sleep(5)
    post_button = driver.find_element(By.XPATH, "//div[@aria-label='Post']")
    post_button.click()
    print('Posted status!')
except Exception as e:
    print('Could not post status:', e)
      
      

