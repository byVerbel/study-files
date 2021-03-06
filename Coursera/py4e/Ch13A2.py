# The program will prompt for a URL, read the JSON data from that URL using
# urllib and then parse and extract the comment counts from the JSON data, compute
# the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(html), 'characters')

info = json.loads(html)

total = list()
for item in info['comments']:
    num = int(item['count'])
    total.append(num)

print('Count:', len(total))
print('Sum:', sum(total))
