# Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number of lines that
# matched the regular expression:

import re

fname = input("Enter file: ")
if len(fname) < 1 : fname = "mbox.txt"
fh = open(fname)
count = 0
regex = input("Enter regular expression: ")
for line in fh:
    line = line.rstrip()
    if re.search(regex, line):
        count = count + 1

print(fname, 'had', count, 'lines that matched', regex)
