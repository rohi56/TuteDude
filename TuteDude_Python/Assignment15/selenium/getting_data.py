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


products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
for product in products:
    try:
        title_elem = product.find_element(By.XPATH, './/h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]/span')
        title = title_elem.text if title_elem else "Title Not Found"
        print(title)
    except Exception as e:
        print("Error extracting title:", e)

driver.quit()