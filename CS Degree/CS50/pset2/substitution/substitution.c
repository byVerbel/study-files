// Program that encrypts letters

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Prototype function
char getSubstitute(char letter, char key[]);

int main(int argc, string argv[])
{
    // Check for correct input in the terminal
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    else if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    else
    {
        for (int i = 0; i < 26; i++)
        {
            int charAscii = (int) argv[1][i];

            // Check that the key contains alphabet characters
            if (!((charAscii >= 65 && charAscii <= 90) || (charAscii >= 97 && charAscii <= 122)))
            {
                printf("Key must contain alphabet characters.\n");
                return 1;
            }

            // Check there aren't duplicate characters
            for (int j = i + 1; j < 26; j++)
            {
                int otherAscii = (int) argv[1][j];
                if (charAscii == otherAscii)
                {
                    printf("Key must not contain duplicate characters.\n");
                    return 1;
                }
            }
        }

        // Prompt user for string
        string text = get_string("plaintext: ");
        printf("ciphertext: ");

        // Make ciphertext
        for (int i = 0, n = strlen(text); i < n; i++)
        {
            int characterAscii = (int) text[i];
            if (characterAscii >= 65 && characterAscii <= 90)
            {
                printf("%c", toupper(getSubstitute(text[i], argv[1])));
            }
            else if (characterAscii >= 97 && characterAscii <= 122)
            {
                printf("%c", tolower(getSubstitute(text[i], argv[1])));
            }
            else
            {
                printf("%c", (char) characterAscii);
            }
        }
        printf("\n");
        return 0;
    }
}

// Method that returns the encrypted letter
char getSubstitute(char letter, char key[])
{
    char capital = toupper(letter);
    int capitalAscii = (int) capital;
    int keySubstitute = capitalAscii - 65;
    char substitute = key[keySubstitute];
    return substitute;
}