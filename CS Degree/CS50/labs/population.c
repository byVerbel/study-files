#include <cs50.h>
#include <stdio.h>

int llamasBorn(int n);
int llamasDeceased(int n);

int main(void)
{
    // TODO: Prompt for start size
    int startSize;
    do
    {
        startSize = get_int("Start size: ");
    }
    while (startSize < 9);

    // TODO: Prompt for end size
    int endSize;
    do
    {
        endSize = get_int("End size: ");
    }
    while (endSize < startSize);

    // TODO: Calculate number of years until we reach threshold
    int yearsUntilThreshold = 0;
    int currentSize = startSize;

    while (currentSize < endSize)
    {
        currentSize = currentSize + llamasBorn(currentSize) - llamasDeceased(currentSize);
        yearsUntilThreshold++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", yearsUntilThreshold);
}

// Define method for amount of new llamas per year
int llamasBorn(int n)
{
    int born = n / 3;
    return born;
}

// Define method for amount of dead llamas per year
int llamasDeceased(int n)
{
    int deceased = n / 4;
    return deceased;
}