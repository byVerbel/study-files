# Revise a previous program as follows: Read and parse the “From” lines and pull
# out the addresses from the line. Count the number of messages from each person
# using a dictionary.
#
# After all the data has been read, print the person with the most commits by
# creating a list of (count, email) tuples from the dictionary. Then sort the
# list in reverse order and print out the person who has the most commits.

fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
counts = {}

for line in fh:
    stripline = line.rstrip()
    if not stripline.startswith("From"):
        continue
    if stripline.startswith("From:"):
        continue
    splitline = stripline.split()
    person = splitline[1]
    counts[person] = counts.get(person, 0)+1

flist = sorted([(v, k) for k, v in counts.items()], reverse=True)

for count, person in flist:
    print(person, count)
    break
