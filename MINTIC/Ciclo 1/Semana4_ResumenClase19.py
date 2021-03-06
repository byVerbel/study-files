import numpy as np
from numpy import prod


"""

Porque Numpy: Esta diseñado para mejorar el rendimiento cuando se trata de hacer calculos
a volumnes grandes de datos.
	*	es distinta, y mucho más eficiente, la manera en que se accede a los elementos 
		de un array de NumPy con respecto a como Python procede a realizar tal tarea en sus estructuras de datos básicas
	*	el número de comprobaciones intermedias a la hora de llevar a cabo cálculos numéricos es menor en NumPy.
	*	NumPy está escrito utilizando el lenguaje de programación C, que es bastante más rápido que Python.
	*	Ordenar los miembros de un arreglo
	*	Operaciones matemáticas y lógicas.
	*	Funciones de entrada / salida
	*	Operaciones estadísticas y de álgebra lineal.


números objeto de alto nivel: enteros, de punto flotante
contenedores: listas (inserción y agregar elementos), diccionarios (búsqueda rápida)

Numpy dispone lo siguiente: 	
paquete de extensión Python para matrices multidimensionales
cercano al hardware (eficiente)
diseñado para cálculo científico (conveniente) 

	


																	"""


def factorial(n):
        print (prod(range(1,n+1)))
factorial(60)



a = np.array([34, 25, 7])
print(type(a))


lista = [23,45,4545,454,23,78,990]
b = np.array(lista)
print('tipo lista : ')
print(type(lista))
print('tipo numpy : ')
print(type(b)) 


print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
objeto_numpy =  np.array([
							[0, 1, 2],
              				[3, 4, 5],
              				[6, 7, 8],
              				[9, 10, 11]
              			])

print(objeto_numpy[2][2])


objeto_21 = np.array(
							[0, 1, 2]
              			) 


print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
# crea Matriz de ceros
print('crea Matriz de ceros')
matriz = np.zeros((3,3))   
print(matriz) 

print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
# Matriz identidad
print('crea Matriz identidad')
d = np.eye(3)         
print(d) 


print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')

# Función Shape // Dimension 
print('Shape:')
print(objeto_numpy.shape)


print('Shape objeto 21:')
print(objeto_21.shape)

print('Shape ndim 21:')
print(objeto_21.ndim)


print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')

print('funciones de crerar objeto a partie de otro')
objeto2 = np.array([
					[1,2,3,4], 
					[5,6,7,8], 
					[9,10,11,12]
				])
objeto2_2 = objeto2[:3, 1:4]

print('objeto2 :')
print(objeto2)
print('objeto2_2 :')
print(objeto2_2)

print("sacar valor 3,4")
print(objeto2[2,2])

print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
print('Indexación de matrices de enteros:')


print(np.arange(0,7))

		



print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
print('Indexación de matrices de boleanos:')

objeto_bool = np.array([
						[1,2], 
						[3, 4], 
						[5, 6]
					])
bool_condicion = (objeto_bool > 1)

print(bool_condicion) 





print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
# los tipos de datos dentro de un objeto numpy deben se del mismo tipo
print('Tipos de datos:')

tipe_int = np.array([1, 2])   # Dejar que numpy elija el tipo de datos
print(tipe_int.dtype)


type_float = np.array([1.0, 2.0])   # Dejar que numpy elija el tipo de datos
print(type_float.dtype)



print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
# 
print('funciones en matrices')

print('adicion')
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
#print(x + y)
print(np.add(x, y))


print('Diferencia')

print(x - y)
print(np.subtract(x, y))



print('Producto')
print(x * y)
print('Producto version 2')
print(np.multiply(x, y))

print('Division')
print(x / y)
print(np.divide(x, y))

print('Raiz Cuadrada')
print(np.sqrt(x))




print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
# 
print('MAtriz inversa')

x = np.array([[1,2],[3,4]]) 
y = np.linalg.inv(x) 
print(x) 
print(y) 
print (np.dot(x,y))





print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
# 
print('Broadcasting')

x = np.array([
			[1,2,3], 
			[4,5,6], 
			[7,8,9], 
			[10, 11, 12]
		])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # Crear una matriz vacía con la misma forma que x


for i in range(4):
    y[i, :] = x[i, :] + v

print('matriz x')
print(x)
print('matriz y')
print(y)





                             							