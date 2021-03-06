# In this assignment you will write a Python program somewhat similar to
# http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read
# the XML data from that URL using urllib and then parse and extract the comment
# counts from the XML data, compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(html), 'characters')

tree = ET.fromstring(html)
lst = tree.findall('.//count')
print('Count:', len(lst))

total = list()
for item in lst:
    num = item.text
    num = int(num)
    total.append(num)

print('Sum:', sum(total))
