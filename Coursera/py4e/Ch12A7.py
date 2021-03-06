# The program will use urllib to read the HTML from the data files below, extract
# the href= vaues from the anchor tags, scan for a tag that is in a particular
# position relative to the first name in the list, follow that link and repeat
# the process a number of times and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
position = int(input('Enter position - '))
loops = int(input('Enter loops - '))
for i in range(loops):
    print(tags[position-1].contents[0])
    if i==loops-1: break
    url = tags[position-1].get('href', None)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
print('Last name', tags[position-1].contents[0])
