# Programa que simula lanzamientos de dados (desde 1 hasta 10 dados).
# Los dados podrá dar el resultado en el rango que el usuario desee.

import math
import random

a = input('Número mínimo:')
b = input('Número máximo:')
c = input('Número de dados:')
try:
    a = int(a)
    b = int(b)
    c = int(c)
except:
    print('Por favor ingrese números')
    quit()
if c>0:
    pass
else:
    print('Por favor ingrese un número de dados positivo')
    quit()
if a<b:
    pass
else:
    print('El número máximo debe ser mayor que el mínimo')
    quit()

while c>0:
    print(random.randint(a,b))
    c = c-1
print('¡Hecho!')
