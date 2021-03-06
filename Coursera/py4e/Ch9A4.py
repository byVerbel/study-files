# Write a program to read through the mbox-short.txt and figure out who has sent
# the greatest number of mail messages. The program looks for 'From ' lines and
# takes the second word of those lines as the person who sent the mail. The program
# creates a Python dictionary that maps the sender's mail address to a count of
# the number of times they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most
# prolific committer.

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
    mail = splitline[1]
    counts[mail] = counts.get(mail,0)+1
    for word, count in list(counts.items()):
        if max is None or count > max:
            email = word
            max = count
print(email,max)
# or ###########################################################################
# fname = input("Enter file:")
# if len(fname) < 1 : fname = "mbox-short.txt"
# fh = open(fname)
# counts = {}
# max = None
# email = None
# for line in fh:
#     stripline = line.rstrip()
#     if not stripline.startswith("From") : continue
#     if stripline.startswith("From:") : continue
#     splitline = stripline.split()
#     day = splitline[1]
#     counts[day] = counts.get(day,0)+1
#     for word in counts:
#         if max is None or counts[word] > max:
#             email = word
#             max = counts[word]
# print(email,max)
