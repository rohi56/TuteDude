import requests

url = 'https://www.python.org/static/img/python-logo.png'
response = requests.get(url)
print(response.request.headers)
#print(response.content)
pic = response.content
with open('python.png', 'wb') as f:
    f.write(pic)