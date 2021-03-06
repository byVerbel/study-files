for i in range(1,101):
    if i in range(0,101,3) and i in range(0,101,5):
        print('FizzBuzz')
    elif i in range(0,101,3):
        print('Fizz')
    elif i in range(0,101,5):
        print('Buzz')
    else:
        print(i)
