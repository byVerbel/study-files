# (Advanced) Change the socket program so that it only shows data after the
# headers and a blank line have been received. Remember that recv receives
# characters (newlines and all), not lines.

import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    url = input('Insert URL: ')
    if url == 'done' : quit()
    parse = url.split('/')
    if len(parse)<1: continue
    if re.match('http[s]?:', parse[0].lower()):
        link = parse[2]
    else:
        link = parse[0]
    # test if the url works
    try:
        mysock.connect((link, 80))
        break
    except:
        print('Please insert a valid URL')
        continue

cmd = f'GET {url} HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)
count = 0

resp = []
while True:
    data = mysock.recv(200)
    if not data: break
    resp.append(data.decode())

resp = "".join(resp)
body = resp.split('\r\n\r\n')[1]
print(body)
mysock.close()
