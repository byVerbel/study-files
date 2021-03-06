# Programa que simula lanzamientos de dados (desde 1 hasta 10 dados).
# Los dados podrá dar el resultado en el rango que el usuario desee.

import math
import random
d = 0
while True:
    c = input('Number of dices:')
    if c == 'Done':
        break
    try:
        c = int(c)
    except:
        print('Please enter numbers')
        continue
    if c>0:
        pass
    else:
        print('Please enter at least 1 dice')
        continue
    while c>0:
        print(random.randint(1,6))
        c = c-1
    d = d+1
    print('Number of times you have rolled the dice:',d)
print('Finished')

#Ahora quiero que haya un contador de tiempo, que el programa se quite si hay
#inactividad por un determinado tiempo.
#
#También quiero que la aplicación abra una ventana nueva por si misma con una
#buena interfaz.
