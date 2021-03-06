# Write a program which repeatedly reads numbers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try
# and except and print an error message and skip to the next number.

c = 0
t = 0
while True:
    x = input('Enter number:')
    if x == 'done':
        break
    try:
        n = float(x)
    except:
        print('Please enter number')
        continue
    t = t+n
    c = c+1
    a = t/c
if c>0:
    print(t, c, a)
else:
    print('No numbers entered')
