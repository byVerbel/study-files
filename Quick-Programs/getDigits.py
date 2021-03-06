## In this file I'm gonna get every digit of a number by using module

# Define function that gives me the digit I want
def getDigit(num: int, mod: int) -> int:
    digit = (num%mod)//(mod//10)
    return digit

while True:
    # Input credit card number
    creditNumber = input("Number: ")
    try:
        creditNumericValue = int(creditNumber)
        if creditNumericValue > 0:
            pass
        else:
            continue
    except:
        # Exit program
        if creditNumber == 'done':
            break
        else:
            continue
        
    creditDigits = len(creditNumber)
    print("Your number has", creditDigits, "digits.\n")

    while True:
        # Input digit to get from left to right
        digitWanted = input("What digit do you want to get? (from left to right) ")
        try:
            digitWanted = int(digitWanted)
            if digitWanted > 0 and digitWanted <= creditDigits:
                break
            else:
                continue
        except:
            continue
    
    # Conversion before creating the module
    digitWanted = creditDigits - digitWanted + 1
    module = 10**digitWanted

    digitValue = getDigit(creditNumericValue, module)

    print("The digit in that position is:", digitValue)

