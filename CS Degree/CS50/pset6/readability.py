text = input("Text: ")

# Initialize variables
letters = sentences = 0
words = 1

# Count letters, words and sentences
for i in range(len(text)):
    letterAscii = ord(text[i])
    if letterAscii == 32:
        words += 1
    elif letterAscii in [33, 46, 63]:
        sentences += 1
    elif (letterAscii in range(65, 91)) or (letterAscii in range(97, 123)):
        letters += 1

# Calculate Coleman-Liau index
averageLetters = letters * 100.0 / words
averageSentences = sentences * 100.0 / words
index = round((0.0588 * averageLetters) - (0.296 * averageSentences) - 15.8)

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print("Grade", index)
