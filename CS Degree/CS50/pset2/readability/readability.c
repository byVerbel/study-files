#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
    // Get text from the user
    string text = get_string("Text: ");

    // Initialize letters, words and sentences counts
    int letters = 0;
    int words = 1;
    int sentences = 0;

    // Count letters, words and sentences
    for (int i = 0, characters = strlen(text); i < characters; i++)
    {
        int letterAscii = (int) text[i];
        if (letterAscii == 32)
        {
            words++;
        }
        else if (letterAscii == 33 || letterAscii == 46 || letterAscii == 63)
        {
            sentences++;
        }
        else if ((letterAscii >= 65 && letterAscii <= 90) || (letterAscii >= 97 && letterAscii <= 122))
        {
            letters++;
        }
    }

    // Print results
    // printf("%i letter(s)\n", letters);
    // printf("%i word(s)\n", words);
    // printf("%i sentence(s)\n", sentences);

    // Calculate Coleman-Liau index
    float averageLetters = (letters * 100.0) / words;
    float averageSentences = (sentences * 100.0) / words;
    int index = round((0.0588 * averageLetters) - (0.296 * averageSentences) - 15.8);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}