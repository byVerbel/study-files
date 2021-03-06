# Write a program to read through the mail box data and when you find line that
# starts with “From”, you will split the line into words using the split function.
# We are interested in who sent the message, which is the second word on the From line.

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    stripline = line.rstrip()
    if not stripline.startswith("From") : continue
    if not stripline.startswith("From:") : continue
    splitline = stripline.split()
    count = count+1
    print(splitline[1])
print("There were", count, "lines in the file with From as the first word")
