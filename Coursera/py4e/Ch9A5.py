# This program records the domain name (instead of the address) where the message
# was sent from instead of who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.

fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
counts = {}
max = None
email = None
for line in fh:
    stripline = line.rstrip()
    if not stripline.startswith("From") : continue
    if stripline.startswith("From:") : continue
    splitline = stripline.split()
    address = splitline[1].split('@')
    domain = address[1]
    counts[domain] = counts.get(domain,0)+1

print(counts)
