# Write a program to prompt for a score between 0.0 and 1.0. If the score is out
# of range, print an error message. If the score is between 0.0 and 1.0, print a
# grade using the following table:

score = input("Enter Score: ")
try:
    nscore = float(score)
except:
    print('Bad input. Please enter a number.')
    quit()
if nscore > 1:
    print('Bad input. Please enter a number between 0 and 1.')
elif nscore >= 0.9:
    print ('A')
elif nscore >= 0.8:
    print('B')
elif nscore >= 0.7:
    print ('C')
elif nscore >= 0.6:
    print ('D')
elif nscore > 0:
    print ('F')
else:
    print ('Bad input. Please enter a number between 0 and 1.')
