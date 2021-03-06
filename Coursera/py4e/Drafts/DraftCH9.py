# names = ['csev','cwen','csev','zqian','cwen']
# count ={}
# for freq in names:
#     if freq not in count:
#         count[freq] = 1
#         continue
#     count[freq] = count[freq]+1
# print(count)
#
# names = ['csev','cwen','csev','zqian','cwen']
# count ={}
# for freq in names:
#     count[freq]=count.get(freq,0)+1
#
# print(count)
################################################################################
# pan = "Words2.txt"
# texto = open(pan)
# keys = {}
# for line in texto:
#     words = line.split()
#     for word in words:
#         if word not in keys:
#             keys[word] = ''
# print(keys)
################################################################################
# fname = "mbox-short.txt"
# fh = open(fname)
# count = {}
# for line in fh:
#     stripline = line.rstrip()
#     if not stripline.startswith("From") : continue
#     if stripline.startswith("From:") : continue
#     splitline = stripline.split()
#     day = splitline[2]
#     count[day] = count.get(day,0)+1
# print(count)
################################################################################
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)
