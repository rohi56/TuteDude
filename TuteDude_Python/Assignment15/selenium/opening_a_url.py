from selenium import webdriver
from selenium.webdriver.edge.service import Service

service = Service('C:/Program Files (x86)/Internet Explorer/edgedriver_win64/msedgedriver.exe')
driver = webdriver.Edge(service=service)
driver.get("https://en.wikipedia.org")
input("Press Enter to close the browser...")