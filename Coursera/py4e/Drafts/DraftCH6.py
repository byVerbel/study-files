# fruit = 'banana'
# index = 0
# lenght = len(fruit)
# #print each letter of the string
# print('Straight')
# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index = index + 1
# #print each letter of the string backwards
# print('Backwards')
# while lenght > 0:
#     letter = fruit[lenght-1]
#     print(letter)
#     lenght = lenght-1
################################################################################
# txt = "Hello, welcome to my world."
# x = txt.find("welcome")
# print(x)
# x = txt.find("e")
# print(x)
# x = txt.find("e", 5, 10)
# print(x)
# print(txt.find("q"))
# print(txt.index("q")) #Traceback
################################################################################
# str1 = "Hello"
# str2 = 'there'
# bob = str1 + str2
# print(bob)
################################################################################
# x = '40'
# y = int(x) + 2
# print(y)
################################################################################
# x = 'From marquard@uct.ac.za'
# print(x[8])
# print(x[14:17])
################################################################################
# print(len('banana')*7)
################################################################################
# greet = 'Hello Bob'
# print(greet.upper())
################################################################################
# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# pos = data.find('.')
# print(data[pos:pos+3])
################################################################################
# word = 'banana'
# nword = word.count('a')
# print(nword)
################################################################################
# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
# print(x)
################################################################################
# txt = "hello, my name is Peter, I am 26 years old"
# x = txt.split(", ")
# print(x)
################################################################################
# zot = 'abc'
# print(zot[0:5])
################################################################################
# fruit = 'banana'
# print(fruit[3:3])
################################################################################
# word = input('Please insert a word:')
# if word < 'banana':
#     print('Your word, ' + word + ', comes before banana.')
# elif word > 'banana':
#     print('Your word, ' + word + ', comes after banana.')
# else:
#     print('All right, bananas.')
################################################################################
# line = '''      Here
#  we
#   go  '''
# print(line.strip())
################################################################################
# texto = open('Words.txt')
# for strn in texto:
#     line = str(strn).rstrip()
#     print(line)
#     nline = line.lower()
#     print(line.capitalize())
