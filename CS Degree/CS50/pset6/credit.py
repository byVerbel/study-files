# from cs50 import get_string

# Insert credit card number
while True:
    creditNumber = input("Number: ")
    if not int(creditNumber) < 0:
        break

# Initialize total
total = 0

# Calculate Luhn’s algorithm
for i in range(-1, -len(creditNumber) - 1, -1):
    if i % 2 == 0:
        digit = int(creditNumber[i])
        digit *= 2

        if digit >= 10:
            digit = str(digit)
            for j in digit:
                total += int(j)
        else:
            total += digit
    else:
        total += int(creditNumber[i])


# Verify card type
validation = "INVALID"

if total % 10 == 0:
    if len(creditNumber) in [13, 15, 16]:
        if int(creditNumber[0]) == 4:
            validation = "VISA"
        elif int(creditNumber[0:2]) in [34, 37]:
            validation = "AMEX"
        elif int(creditNumber[0:2]) in [51, 52, 53, 54, 55]:
            validation = "MASTERCARD"

print(validation)
