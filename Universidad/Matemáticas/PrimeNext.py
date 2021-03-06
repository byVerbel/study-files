from Primecheck import isprime

def nextprime(num):
    n = num
    while isprime(n)==False:
        n = n+1
    return f'Next prime is {n}'
print(nextprime(21))
print(nextprime(14))
print(nextprime(0))
