def calculateRemainder(number, module):
    digit = (number % module)//(module//10)
    return digit

# Get positive integer from user
while True:
    # Input credit card number
    creditNumber = input("Credit Card number: ")
    try:
        creditNumericValue = int(creditNumber)
        if creditNumericValue > 0:
            break
        else:
            continue
    except:
        # Exit program
        if creditNumber == 'done':
            quit()
        else:
            continue

# Initialize module, even checker, last even number, last odd number and credit card first numbers
module = 10
digitCount = 0
lastEven = 0
lastOdd = 0
startNumber = 0

# Initialize total sum
total = 0

while module <= creditNumericValue * 10:
    digitCount += 1
    digit = calculateRemainder(creditNumericValue, module)
    if digitCount % 2 == 0:
        lastEven = digit
        digit *= 2
        if digit >= 10:
            firstDigit = calculateRemainder(digit, 10)
            secondDigit = calculateRemainder(digit, 100)
            total = total + firstDigit + secondDigit
        else:
            total = (digit) + total
    else:
        lastOdd = digit
        total = digit + total

    module *= 10

# Initialize validation
validation = "INVALID"

if digitCount % 2 == 0:
    startNumber = (lastEven * 10) + lastOdd
else:
    startNumber = (lastOdd * 10) + lastEven

if total % 10 == 0:
    if digitCount == 13 or digitCount == 15 or digitCount == 16 or digitCount == 4:
        if startNumber // 10 == 4:
            validation = "VISA"
        elif startNumber == 34 or startNumber == 37:
            validation = "AMEX"
        elif startNumber == 51 or startNumber == 52 or startNumber == 53 or startNumber == 54 or startNumber == 55:
            validation = "MASTERCARD"

# print(total)
print(validation)
