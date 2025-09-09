import urllib.request, urllib.parse, urllib.error

url = urllib.request.urlopen('http://www.python.org')

for line in url:
    line = line.decode('utf-8').strip()  # Decoding the binary data to text.
    if 'Python' in line:
        print(line)
