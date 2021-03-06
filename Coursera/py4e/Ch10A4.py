# Compare results in Ch10A3.py with the tables at
# https://wikipedia.org/wiki/Letter_frequencies.

import string

fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
counts = {}

for line in fh:
    stripline = line.rstrip()
    if not stripline.startswith("From") : continue
    if stripline.startswith("From:") : continue
    stripline = stripline.translate(str.maketrans('', '', string.punctuation))
    stripline = stripline.translate(str.maketrans('', '', string.digits))
    stripline = stripline.lower()
    stripline = stripline.replace(' ','')
    letters = list(stripline)
    for letter in letters:
        counts[letter] = counts.get(letter,0)+1

flist = sorted([ (v,k) for k,v in counts.items() ], reverse=True)
flist = sorted([ (k,v) for v,k in flist ])

# for k,v in flist:
#     print(k,v)

# find their porcentage

total = 0
porcentage = 0
for letter,count in flist:
    total = total + count
for letter,count in flist:
    porcentage = round(count/total*100,2)
    print(letter,count,porcentage)
