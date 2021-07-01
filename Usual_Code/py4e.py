# Delete all punctuation marks in a text, line, string, etc.
import string  # I can use puntuation or digits

.translate(str.maketrans('', '', string.punctuation))

# Create an istogram
z = []
x = {}
for y in z:
    x[y] = x.get(y, 0)+1
    print(x)

# List comprehension
    print(sorted([(v, k) for k, v in c.items()]))

# Regex searches
    import re
    # use | to avoid traceback if there's no match
    re.findall('\d+|$', 'aa33bbb44')[0]

# Socket
    import socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))

# BeautifulSoup for searches
# Look at the parts of a tag

# Code Snippets: I could make some snippets in VSCode with lines from this file

# Search for consecutive sequences of a string
    pat = "(?:{seq})+".format(seq=STR)
