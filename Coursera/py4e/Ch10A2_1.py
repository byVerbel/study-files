# Write a program to read through the mbox-short.txt and figure out the distribution
# by hour of the day for each of the messages. You can pull the hour out from the
# 'From ' line by finding the time and then splitting the string a second time
# using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

fname = input("Enter file: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
counts = {}

for line in fh:
    stripline = line.rstrip()
    if not stripline.startswith("From") : continue
    if stripline.startswith("From:") : continue
    splitline = stripline.split()
    times = splitline[5].split(':')
    hour = times[0]
    counts[hour] = counts.get(hour,0)+1

# Now I can do this:

flist = list()
for hr,count in counts.items():
    newtup = (hr,count)
    flist.append(newtup)

flist = sorted(flist)

# or this: flist = sorted([ (k,v) for k,v in counts.items() ])

for hr,count in flist:
    print(hr,count)
