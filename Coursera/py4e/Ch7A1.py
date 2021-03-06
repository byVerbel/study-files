# Write a program to read through a file and print the contents of the file
# (line by line) all in upper case. 

txt = input('Enter file name: ')
texto = open(txt)
print(texto.read().upper())
