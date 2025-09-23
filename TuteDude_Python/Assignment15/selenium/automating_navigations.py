from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
service = Service('C:/Program Files (x86)/Internet Explorer/edgedriver_win64/msedgedriver.exe')
driver = webdriver.Edge(service=service)
driver.get("https://www.google.com")
driver.maximize_window()
search_box = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.NAME, "q"))
)
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)


# Wait for a result link (h3) or print a message if not found (possible CAPTCHA)
try:
	WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
	)
	print("Search results loaded.")
except:
	print("No search results found. You may have encountered a CAPTCHA or page structure change.")

driver.back()  # Navigate back to the search page
time.sleep(5)  # Wait for the page to load
driver.forward()  # Navigate forward to the results page
time.sleep(5)  # Wait for the page to load

driver.quit()