# Rewrite the program that prompts the user for a list of numbers and prints out
# the maximum and minimum of the numbers at the end when the user enters “done”.
# Write the program to store the numbers the user enters in a list and use the
# max() and min() functions to compute the maximum and minimum numbers after the
# loop completes.

tist = list()
while True:
    x = input('Enter number:')
    if x == 'done':
        break
    try:
        n = int(x)
    except:
        print('Invalid input')
        continue
    tist.append(n)
if len(tist)>=1:
    print('Maximum is', max(tist))
    print('Minimum is', min(tist))
else:
    print('No numbers entered')
