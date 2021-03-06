// Prints a bricks pyramid

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long x = get_long("x: ");

    long y = get_long("y: ");

    printf("%i\n", (x % y) / (y / 10));
}