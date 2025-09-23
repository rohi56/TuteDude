from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('C:/Program Files (x86)/Internet Explorer/edgedriver_win64/msedgedriver.exe')
driver = webdriver.Edge(service=service)
driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(5)  # Wait for the page to load

driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys("Samsung Galaxy S25 Ultra")
driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()
time.sleep(5)  # Wait for the search results to load
input("Press Enter to close the browser...")