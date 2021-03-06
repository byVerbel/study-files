// Validate credit card number

// #include <cs50.h>
// #include <stdio.h>
// #include <math.h>

long calculateRemainder (long number, long module);

int main(void)
{
    // Get positive integer from user
    long creditNumber;
    do
    {
        creditNumber = get_long("Number: ");
    }
    while (creditNumber < 0);

    // Initialize module, even checker, last even number, last odd number and credit card first numbers
    long module = 10;
    long digitCount = 0;
    long lastEven = 0;
    long lastOdd = 0;
    long creditStart = 0;

    // Initialize total sum
    long total = 0;

    // Check Luhn's Algorithm
    while (module <= creditNumber * 10)
    {
        digitCount++;
        long digit = calculateRemainder(creditNumber, module);
        if (digitCount % 2 == 0)
        {
            lastEven = digit;
            digit *= 2;
            if (digit >= 10)
            {
                long firstDigit = calculateRemainder(digit, 10);
                long secondDigit = calculateRemainder(digit, 100);
                total = total + firstDigit + secondDigit;
            }
            else
            {
                total = total + digit;
            }
        }
        else
        {
            lastOdd = digit;
            total = digit + total;
        }

        module *= 10;
    }

    // printf("Digit count: %li\n", digitCount);
    // printf("Total: %li\n", total);

    // Initialize validation
    string validation = "INVALID";

    // Check if the number is even or odd
    if (digitCount % 2 == 0)
    {
        creditStart = (lastEven * 10) + lastOdd;
    }
    else
    {
        creditStart = (lastOdd * 10) + lastEven;
    }
    // printf("Start number: %li\n", creditStart);

    // Check how many numbers does the ingresed number have (maybe I can do this at the beggining, or in other method)
    if (total % 10 == 0)
    {
        if (digitCount == 13 || digitCount == 15 || digitCount == 16)
        {
            if (creditStart / 10 == 4)
            {
                validation = "VISA";
            }
            else if (creditStart == 34 || creditStart == 37)
            {
                validation = "AMEX";
            }
            else if (creditStart == 51 || creditStart == 52 || creditStart == 53 || creditStart == 54 || creditStart == 55)
            {
                validation = "MASTERCARD";
            }
        }
    }

    printf("%s\n", validation);
}

// Define method that calculates the remainder
long calculateRemainder (long number, long module)
{
    long digit = (number % module) / (module / 10);
    return digit;
}