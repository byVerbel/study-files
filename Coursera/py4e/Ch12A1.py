# Change the socket program socket1.py to prompt the user for the URL so it can
# read any web page. You can use split('/') to break the URL into its component
# parts so you can extract the host name for the socket connect call. Add error
# checking using try and except to handle the condition where the user enters
# an improperly formatted or non-existent URL.

import socket
# import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    url = input('Insert URL: ')
    if url == 'done' : quit()
    parse = url.split('/')
    if len(parse)<1: continue
    # if re.match('http[s]?:', parse[0].lower()):
    if parse[0].lower()=='http:' or parse[0].lower()=='https:':
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

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(),end='')
mysock.close()
