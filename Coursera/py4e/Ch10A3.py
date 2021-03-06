# Write a program that reads a file and prints the letters in decreasing order of
# frequency. Your program should convert all the input to lower case and only
# count the letters a-z. Your program should not count spaces, digits, punctuation,
# or anything other than the letters a-z. Find text samples from several different
# languages and see how letter frequency varies between languages.

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

for count,letter in flist:
    print(letter,count)

# find their porcentage
# 
# total = 0
# porcentage = 0
# for count,letter in flist:
#     total = total + count
# for count,letter in flist:
#     porcentage = round(count/total*100,2)
#     print(letter,count,porcentage)
