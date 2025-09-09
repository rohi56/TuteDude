import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

def Extract(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')  # ✅ use .text instead of the response object
    tag = soup.find_all('h2')
    content = [span.text for span in tag]
    print(content)


    # Write to CSV file
    with open("wikipedia_headings.csv","w") as file:
        writer = csv.writer(file)
        writer.writerow(content)
        
print(Extract('https://en.wikipedia.org/wiki/Main_Page'))