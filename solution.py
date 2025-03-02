import urllib.request
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
total = 0
count = 0

for tag in tags:
    num = int(tag.contents[0])
    total += num
    count += 1

print('Count', count)
print('Sum', total)