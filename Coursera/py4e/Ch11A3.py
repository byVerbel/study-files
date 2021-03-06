# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.

import re

fname = "regex_sum_850941.txt"
fh = open(fname)
total = list()
for line in fh:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    for n in x:
        n = int(n)
        total.append(n)

print(sum(total))
