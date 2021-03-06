#include <stdio.h>
#include <string.h>

void main(void)
{
    char name[4] = {'0', '0', '0'};

    int i = 0;

    while (i < 150)
    {
        char file_name[8];
        strcpy(file_name, name);
        strcat(file_name, ".jpg");
        printf("%s\n", file_name);

        if (name[2] == '9')
        {
            if (name[1] == '9')
            {
                name[0]++;
                name[1] = '0';
                name[2] = '0';
            }
            else
            {
                name[1]++;
                name[2] = '0';
            }
        }
        else
        {
            name[2]++;
        }

        i++;
    }
}