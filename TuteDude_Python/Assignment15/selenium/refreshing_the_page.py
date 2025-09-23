from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

service = Service('C:/Program Files (x86)/Internet Explorer/edgedriver_win64/msedgedriver.exe')
driver = webdriver.Edge(service=service)
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
time.sleep(5)  # Wait for the page to load

driver.refresh()  # Refresh the page

input("Press Enter to close the browser...")