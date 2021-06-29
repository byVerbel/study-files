#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

// Number of bytes in JPEG block
const int BLOCK_SIZE = 512;

int main(int argc, char *argv[])
{
    // Ensure valid usage
    if (argc != 2)
    {
        printf("Usage: ./recover cardname.raw\n");
        return 1;
    }

    // Ensure correct forensic file
    char *infile = argv[1];
    char point = '.';
    char *extension = strrchr(infile, point);
    printf("%i\n", strcmp(extension, ".raw"));

    if (strcmp(extension, ".raw") != 0)
    {
        printf("Please insert correct forensic file.");
        return 1;
    }

    // Ensure I can open infile
    FILE *memory = fopen(infile, "r");
    if (memory == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 1;
    }

    // Initialize file names -> The code is in tests
    int file_number = 0;
    uint8_t buffer[BLOCK_SIZE];

    while (fread(buffer, sizeof(uint8_t), BLOCK_SIZE, memory) == BLOCK_SIZE)
    {
        // Restart file name variable
        char file_name[8];

        // Check new JPEG and create next JPEG file name
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] >= 0xe0 && buffer[3] <= 0xef))
        {
            sprintf(file_name, "%03d.jpg", file_number);
            file_number++;
        }

        // Create new JPEG file or update an existing one
        FILE *jpeg_file = fopen(file_name, "a");
        if (jpeg_file == NULL)
        {
            fclose(memory);
            printf("Could not open JPEG file.\n");
            return 1;
        }

        fwrite(buffer, sizeof(uint8_t), BLOCK_SIZE, jpeg_file);

        fclose(jpeg_file);
    }

    fclose(memory);

    return 0;
}