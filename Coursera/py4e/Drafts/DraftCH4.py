# big = max('1 2 3')
# print(big)
# small = min('1 2 3')
# print(small)
################################################################################
# a = 'arroz'
# b = ' con'
# c = ' leche'
# d = a+b+c
# print(d)
################################################################################
# def stuff():
#     print('Hello')
#     return
#     print('World')
# stuff()
################################################################################
# def addtwo(a, b):
#     added = a + b
#     return a
#
# x = addtwo(2, 7)
# print(x)
################################################################################
import math
################################################################################
# print(4/2)
# for i in range(5):
#     print(i)
#     if i>2:
#         print('bigger than 2')
#     else:
#         print('smaller than 2')
################################################################################
# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')
# print(print_lyrics)
# print(type(print_lyrics))
################################################################################
# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')
# repeat_lyrics()
################################################################################
# x = math.cos(radians)
# golden = (math.sqrt(5) + 1) / 2
# print(x)
################################################################################
# def print_twice(arroz):
#     print(arroz)
#     print(arroz)
# result = print_twice('Bing')
# print(result)
# print(type(result))
# x = False
# y = True
# z = x*y
# print(z)
################################################################################
score = input("Enter Score: ")
try:
    nscore = float(score)
except:
    print('Bad input. Please enter a number.')
    quit()

def computegrade(sco):
    if sco > 1:
        return 'Bad input. Please enter a number between 0 and 1.'
    elif sco >= 0.9:
        return 'A'
    elif sco >= 0.8:
        return 'B'
    elif sco >= 0.7:
        return 'C'
    elif sco >= 0.6:
        return 'D'
    elif sco > 0:
        return 'F'
    else:
        return 'Bad input. Please enter a number between 0 and 1.'

print(computegrade(nscore))
