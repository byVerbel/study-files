# Change your socket program so that it counts the number of characters it has
# received and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of
# characters and display the count of the number of characters at the end of the
# document.

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
while True:
    data = mysock.recv(500)
    if (len(data) < 1):
        break
    count = count + len(data)
    print(data.decode(),end='')
    if count >= 3000:
        break

print(count, 'characters retrieved')
mysock.close()
