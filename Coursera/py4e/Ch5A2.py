# Write another program that prompts for a list of numbers as above and at the end
# prints out both the maximum and minimum of the numbers instead of the average.

smallest = None
biggest = None
c = 0
while True:
    x = input('Enter number:')
    if x == 'done':
        break
    try:
        n = int(x)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest = n
    elif n<smallest:
        smallest = n
    if biggest is None:
        biggest = n
    elif n>biggest:
        biggest = n
    c = c+1
if c>0:
    print('Maximum is', biggest)
    print('Minimum is', smallest)
else:
    print('No numbers entered')
