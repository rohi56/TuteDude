from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service('C:/Program Files (x86)/Internet Explorer/edgedriver_win64/msedgedriver.exe')
driver = webdriver.Edge(service=service)
driver.get("https://www.wikipedia.org/")
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "search"))
)
search_box.send_keys("Selenium (software)")
search_box.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".cdx-text-input__input.mw-searchInput"))
)
print("Wikipedia search completed.")

input("Press Enter to close the browser...")
