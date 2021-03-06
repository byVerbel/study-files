# Use urllib to replicate the previous exercise of (1) retrieving the document
# from a URL, (2) displaying up to 3000 characters, and (3) counting the overall
# number of characters in the document. Don’t worry about the headers for this
# exercise, simply show the first 3000 characters of the document contents.

# Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx)#.read()

count = 0
while True:
    data = html.read(500)
    if (len(data) < 1): break
    count = count + len(data)
    print(data.decode(),end='')
    if count >= 3000: break

print(count, 'characters retrieved')
