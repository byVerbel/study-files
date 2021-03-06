# Download a copy of the file www.py4e.com/code3/romeo.txt. Write a program to
# open the file romeo.txt and read it line by line. For each line, split the line
# into a list of words using the split function. For each word, check to see
# if the word is already in a list. If the word is not in the list, add it to the
# list. When the program completes, sort and print the resulting words in
# alphabetical order.

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    stripline = line.rstrip()
    splitline = stripline.split()
    for word in splitline:
        if word in lst : continue
        lst.append(word)
lst.sort()
print(lst)
