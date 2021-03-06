# The program will use urllib to read the HTML from the data files below, and
# parse the data, extracting numbers and compute the sum of the numbers in the file.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
total = list()
for tag in tags:
    tag = str(tag)
    num = re.findall('[0-9]+', tag)[0]
    total.append(int(num))

print('Count', len(tags))
print('Sum', sum(total))
