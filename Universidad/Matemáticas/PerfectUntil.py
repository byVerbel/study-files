from PerfectCheck import isPerfect

def PerfectUntil(num:int)->bool:
    if num >= 1:
        for i in range(1,num+1):
            if isPerfect(i):
                print(i)
        if i>=6:
            return True
        else:
            return False
    else:
        return False

number = input('Please enter number: ')
try:
    number = int(number)
except:
    print('Please insert a number.')

PerfectUntil(number)
