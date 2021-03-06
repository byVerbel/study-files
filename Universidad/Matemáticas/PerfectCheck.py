def isPerfect(num):
    divisors = list()
    # Check that number is bigger than 1
    if num >= 1:
        for i in range(1,(num//2)+1):
            if (num % i) == 0:
                divisors.append(i)
    else:
        return False
        # return 'Please insert a natural number.'

    checklist = list()
    check = sum(divisors)
    for i in divisors:
        stri = str(i)
        checklist.append(stri)
    if check==num:
        return True
        prove = '+'.join(checklist)+' '+'='+' '+str(num)
        # return f'\n{num} is perfect.\n{prove}'
    else:
        return False
        prove = '+'.join(checklist)+' '+'!='+' '+str(num)
        # return f'\n{num} is not perfect.\n{prove}'

# number = input('Please enter number: ')
# try:
#     number = int(number)
# except:
#     print('Please insert a number.')
#
# print(isPerfect(number))
