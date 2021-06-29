// Prints a bricks pyramid

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get positive integer from user
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    // Define the number of spaces in every tier
    int spaces = n - 1;

    // Loop for tiers of the pyramid
    for (int i = 0; i < n; i++)
    {
        // Loop to construct tiers of first pyramid
        for (int j = 0; j < n; j++)
        {
            if (j < spaces - i)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("  ");
        // Loop to construct tiers of second pyramid
        for (int k = 0; k < i + 1; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}