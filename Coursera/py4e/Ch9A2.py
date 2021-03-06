# Write a program that categorizes each mail message by which day of the week the
# commit was done. To do this look for lines that start with “From”, then look for
# the third word and keep a running count of each of the days of the week. At the
# end of the program print out the contents of your dictionary (order does not matter).

fname = "mbox-short.txt"
fh = open(fname)
count = {}
for line in fh:
    stripline = line.rstrip()
    if not stripline.startswith("From") : continue
    if stripline.startswith("From:") : continue
    splitline = stripline.split()
    day = splitline[2]
    count[day] = count.get(day,0)+1
print(count)
