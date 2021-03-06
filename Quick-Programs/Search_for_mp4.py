# import requests
import re
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
links = [link.get('href') for link in soup.find_all('a')]

# Search for videos in tags
videos = []
for link in links:
  match = re.search('.*mp4.*', link)
  if match:
    videos.append(link)

print(videos)
# def downloadfile(name,url):
#     name=name+".mp4"
#     r=requests.get('url')
#     print "****Connected****"
#     f=open(name,'wb');
#     print "Donloading....."
#     for chunk in r.iter_content(chunk_size=255):
#         if chunk: # filter out keep-alive new chunks
#             f.write(chunk)
#     print "Done"
#     f.close()
