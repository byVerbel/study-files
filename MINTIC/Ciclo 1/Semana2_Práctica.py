# Leer un número entero de dos dígitos menor que 20 y determinar si es primo.

try:
    num = int(input("Ingrese un número: "))
except:
    print('Por favor ingrese un número.')
    quit()

if len(str(num))==2 and num<20:
    pass
else:
    print('Por favor ingrese número de 2 dígitos y menor que 20.')
    quit()

for i in range(2,num):
    if (num % i) == 0:
        print(num,"no es un número primo.")
        print(i,"por",num//i,"es",num,'\b.')
        break
else:
    print(num,"es un número primo.")
