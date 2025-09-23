from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('C:/Program Files (x86)/Internet Explorer/edgedriver_win64/msedgedriver.exe')
driver = webdriver.Edge(service=service)
driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(5)  # Wait for the page to load

select = driver.find_element(By.LINK_TEXT, "Electronics")
select.click()
time.sleep(5)  # Wait for the page to load

select_audio = driver.find_element(By.LINK_TEXT, "Audio")
select_audio.click()
input("Press Enter to close the browser...")
