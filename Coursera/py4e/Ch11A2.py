# Write a program to look for lines of the form:
#       New Revision: 39772
# Extract the number from each of the lines using a regular expression and the
# findall() method. Compute the average of the numbers and print out the average
# as an integer.

import re

fname = input("Enter file: ")
if len(fname) < 1 : fname = "mbox.txt"
fh = open(fname)
total = list()
for line in fh:
    line = line.rstrip()
    x = re.findall('^N.+?: ([0-9]+)', line)
    for n in x:
        n = int(n)
        total.append(n)

print(sum(total)//len(total))
