import requests
import re
import os

headers = {
     'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36'
}

user = input("Enter the name of the image you want to download: ")
url = f"https://www.google.com/search?q={user}&sca_esv=453f87096d44fbd1&udm=2&biw=1366&bih=633&sxsrf=AE3TifOMlffJNuMsUPkS6DL2Ofdrr0oEwA%3A1757377697014&ei=oXS_aKFTv-Ox4w_U_Z7pCw&ved=0ahUKEwjhp_eKtsqPAxW_cWwGHdS-J70Q4dUDCBE&oq=moon&gs_lp=EgNpbWciBG1vb24yBxAjGCcYyQIyBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB5IuxpQAFgAcAF4AJABAJgBAKABAKoBALgBDMgBAJgCAaACDZgDAIgGAZIHATGgBwCyBwC4BwDCBwMzLTHIBwg&sclient=img"
response = requests.get(url = url, headers=headers).text

# Pattern to match only .jpg images in the specified format
pattern = r'\["(https://[^\"]+\.jpg)",(\d+),(\d+)\]'
images = re.findall(pattern, response)

print(f"Found {len(images)} images.")

image_count = int(input("Enter the number of images you want to download: "))

if images:
     if not os.path.exists(user):
          os.mkdir(user)
          os.chdir(user)
          
     else :
          os.chdir(user)
     for image in images[:image_count]:
          image_url = image[0]
          response = requests.get(image_url).content
          image_name = image_url.split("/")[-1]
          
          with open(image_name, 'wb') as file:
               file.write(response)
          