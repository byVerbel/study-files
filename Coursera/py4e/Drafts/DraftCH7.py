# neww = '''hola\n
# pipa'''
# print(neww)
# print(len(neww))
################################################################################
txt = input('Por favor ingrese texto:\b')
texto = open(txt)
# No_lines = 0
# for lines in texto:
#     No_lines = No_lines + 1
#     print(lines,"Line lenght:", len(lines))
# print('Total lines in the text:', No_lines)
print(len(texto.read()))
# print(dir(texto))
# print(type(texto))
