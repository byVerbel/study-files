#include "helpers.h"
#include <math.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// Convert image to grayscale
// rgbtBlue rgbtGreen rgbtRed
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float average = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0;
            BYTE gray = round(average);
            image[i][j].rgbtBlue = gray;
            image[i][j].rgbtGreen = gray;
            image[i][j].rgbtRed = gray;
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2.0; j++)
        {
            temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Initialize total and count values
            bool validation;
            float pixelCount = 0.0;
            int totalBlue = 0;
            int totalGreen = 0;
            int totalRed = 0;

            for (int heightOperator = -1; heightOperator <= 1; heightOperator++)
            {
                for (int widthOperator = -1; widthOperator <= 1; widthOperator++)
                {
                    // Find pixels around the pixel of analysis
                    int pixelHeight = i + heightOperator;
                    int pixelWidth = j + widthOperator;

                    // Check border
                    if (pixelHeight < 0 || pixelWidth < 0 || pixelHeight > height - 1 || pixelWidth > width - 1)
                    {
                        validation = false;
                    }
                    else
                    {
                        totalBlue += image[pixelHeight][pixelWidth].rgbtBlue;
                        totalGreen += image[pixelHeight][pixelWidth].rgbtGreen;
                        totalRed += image[pixelHeight][pixelWidth].rgbtRed;
                        pixelCount++;
                    }
                }
            }

            // Blur pixel
            temp[i][j].rgbtBlue = round(totalBlue / pixelCount);
            temp[i][j].rgbtGreen = round(totalGreen / pixelCount);
            temp[i][j].rgbtRed = round(totalRed / pixelCount);
        }
    }

    memcpy(image, temp, sizeof(temp));

    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    // Inititalize kernels
    int GxMatrix[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int GyMatrix[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Initialize values
            bool validation;
            float GxBlue = 0.0;
            float GyBlue = 0.0;
            float GxGreen = 0.0;
            float GyGreen = 0.0;
            float GxRed = 0.0;
            float GyRed = 0.0;
            int GBLUE;
            int GGREEN;
            int GRED;

            for (int a = 0; a < 3; a++)
            {
                for (int b = 0; b < 3; b++)
                {
                    // Find pixels around the pixel of analysis
                    int pixelHeight = i + a - 1;
                    int pixelWidth = j + b - 1;

                    // Check border and get out
                    if (pixelHeight < 0 || pixelWidth < 0 || pixelHeight > height - 1 || pixelWidth > width - 1)
                    {
                        validation = false;
                    }
                    else
                    {
                        // Calculate Gx and Gy values
                        GxBlue += GxMatrix[a][b] * image[pixelHeight][pixelWidth].rgbtBlue;
                        GyBlue += GyMatrix[a][b] * image[pixelHeight][pixelWidth].rgbtBlue;
                        GxGreen += GxMatrix[a][b] * image[pixelHeight][pixelWidth].rgbtGreen;
                        GyGreen += GyMatrix[a][b] * image[pixelHeight][pixelWidth].rgbtGreen;
                        GxRed += GxMatrix[a][b] * image[pixelHeight][pixelWidth].rgbtRed;
                        GyRed += GyMatrix[a][b] * image[pixelHeight][pixelWidth].rgbtRed;
                    }
                }
            }

            // Combine Gx and Gy
            GBLUE = round(sqrt(pow(GxBlue, 2) + pow(GyBlue, 2)));
            GGREEN = round(sqrt(pow(GxGreen, 2) + pow(GyGreen, 2)));
            GRED = round(sqrt(pow(GxRed, 2) + pow(GyRed, 2)));

            // Check if G values are higher than 255 for every color
            GBLUE = (GBLUE > 255) ? 255 : GBLUE;
            GGREEN = (GGREEN > 255) ? 255 : GGREEN;
            GRED = (GRED > 255) ? 255 : GRED;

            // Edge pixel
            temp[i][j].rgbtBlue = GBLUE;
            temp[i][j].rgbtGreen = GGREEN;
            temp[i][j].rgbtRed = GRED;
        }
    }

    memcpy(image, temp, sizeof(temp));

    return;
}

/** Replaces temporal triple in the original
 * CORRECTION: Instead of doing this, I will use memcpy() from the <string.h> header **/
/**void replaceTemp(int h, int w, RGBTRIPLE array[h][w], RGBTRIPLE replacement[h][w])
{
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            array[i][j] = replacement[i][j];
        }
    }

    return;
}**/