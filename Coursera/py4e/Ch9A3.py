# Write a program to read through a mail log, build a histogram using a dictionary
# to count how many messages have come from each email address, and print the dictionary.

fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
counts = {}
for line in fh:
    stripline = line.rstrip()
    if not stripline.startswith("From") : continue
    if stripline.startswith("From:") : continue
    splitline = stripline.split()
    day = splitline[1]
    counts[day] = counts.get(day,0)+1
print(counts)
