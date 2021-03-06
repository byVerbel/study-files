#include <stdio.h>
#include <string.h>

void main(void)
{
    int file_number = 0;

    int i = 0;

    for (int i = 0; i < 150; i++)
    {
        char name[7];
        sprintf(name, "%03d.jpg", file_number);
        printf("%s\n", name);
        file_number++;
    }
}