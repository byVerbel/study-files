# Program to check if a number is prime or not

# try:
#     num = int(input("Enter number: "))
# except:
#     print('Please enter a number.')
#     quit()

# prime numbers are greater than 1
def isprime(num):
    if num > 1:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                # print(num,"is not a prime number")
                return False
                break
        else:
            return True

# if input number is less than
# or equal to 1, it is not prime
    else:
        return False
