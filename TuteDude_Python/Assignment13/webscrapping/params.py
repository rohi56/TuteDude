import requests

url = 'http://www.python.org'
params = {
    'offset': '5'
}
response = requests.get(url, params = params)
print(response.text)
print(response.url)