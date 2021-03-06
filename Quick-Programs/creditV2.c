// Prints a bricks pyramid

// #include <cs50.h>
// #include <stdio.h>
// #include <math.h>

int calculateRemainder (int number, int module);


int main(void)
{
    // Get positive integer from user
    long creditNumber;
    do
    {
        creditNumber = get_long("Input credit number: ");
    }
    while (creditNumber < 0);

    // Initialize module, even checker, last even number, last odd number and credit card first numbers
    int module = 10;
    int digitCount = 1;
    int lastEven = 0;
    int lastOdd = 0;
    int creditStart = 0;

    // Initialize total sum
    int total = 0;

    // Check Luhn's Algorithm
    while (module <= creditNumber)
    {
        if (digitCount % 2 == 0)
        {
            int digit = calculateRemainder(creditNumber, module);
            lastEven = digit;
            total = (digit * 2) + total;
        }
        else
        {
            int digit = calculateRemainder(creditNumber, module);
            lastOdd = digit;
            total = digit + total;
        }

        module *= 10;
        digitCount++;
    }

    // Initialize validation
    string validation = "";

    // Check if the number is even or odd
    if (digitCount % 2 == 0)
    {
        creditStart = lastEven;
    }
    else
    {
        creditStart = (lastOdd * 10) + lastEven;
    }
    
    if ((digitCount == 13 || digitCount == 16) &&
    total == 0 &&
    creditStart == 4)
    {
        validation = "VISA";
    }
    else if (digitCount == 15 &&
    total == 0 &&
    (creditStart == 34 || creditStart == 37))
    {
        validation = "AMEX";
    }
    else if (digitCount == 16 &&
    total == 0 &&
    (creditStart == 51 || creditStart == 52 || creditStart == 53 || creditStart == 54 || creditStart == 55))
    {
        validation = "MASTERCARD";
    }
    else
    {
        validation = "INVALID";
    }
    
    printf("%s\n", validation);
}

// Define method that calculates the remainder
int calculateRemainder (int number, int module)
{
    int digit = (number % module) / (module / 10);
    return digit;
}