import requests

url = 'https://www.w3schools.com/python/demopage.php'

response = requests.post(url)
print(response.text)