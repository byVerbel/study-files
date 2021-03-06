from itertools import permutations

# Defino función para validar distancias positivas en el diccionario
def validacion(distancias:dict):
    for i,j in distancias.keys():
        if distancias[i,j]<0:
            return True
        elif i==j and distancias[i,j]!=0:
            return True
        else:
            pass

def ruteo (distancias: dict, ruta_inicial: list)-> dict:
    if validacion(distancias):
        return 'Por favor revisar los datos de entrada.'
        exit()
    permutacion = permutations(ruta_inicial)
    mejor_distancia = None
    mejor_ruta = 0
    for perm in permutacion:
        ruta = ['H']
        distancia = []
        iteracion = {}
        actual = None
        # Hago un ciclo que no se cierre hasta tener mi nueva ruta
        while len(ruta) != len(perm):
            # Condiciono que mi primera iteración comienza con 'H'
            if actual == None:
                actual = 'H'
            else:
                pass
            # Condiciono que mi último destino es 'H'
            if len(ruta)==len(perm)-1:
                distancia.append(distancias[actual,'H'])
                ruta.append('H')
            else:
                # Recorro las llaves del diccionario
                for i,j in distancias.keys():
                    # Encuentro las llaves que aplican en mi ruta y las agrego a otro diccionario temporal
                    if i == actual and j != actual and j in perm and j not in ruta:
                        iteracion[i,j] = distancias[i,j]
                # Encuentro la distancia mínima
                rmin = min([(dist,rute) for rute,dist in iteracion.items()])
                # Actualizo mi valor actual
                actual = rmin[1][1]
                # Agrego el nodo a mi nueva ruta y agrego la distancia
                ruta.append(rmin[1][1])
                distancia.append(rmin[0])
                # Limpio mi diccionario temporal para la próxima iteración
                iteracion.clear()
        ruta_final = '-'.join(ruta)
        distancia_final = sum(distancia)
        if mejor_distancia==None:
            mejor_distancia = distancia_final
        else:
            if distancia_final<mejor_distancia:
                mejor_ruta = ruta_final
                mejor_distancia = distancia_final
    salida = {'ruta':mejor_ruta,'distancia':mejor_distancia}
    return salida

print(ruteo({('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241, ('A', 'H'):
127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41, ('B', 'H'): 153, ('B', 'A'): 252, ('B',
'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269, ('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C',
'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180, ('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194,
('D', 'F'): 109, ('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119, ('F', 'H'):
267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0},['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']))

print(ruteo({('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27, ('A', 'H'): 72, ('A', 'A'): 0,
('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117, ('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B',
'D'): 126, ('B', 'E'): 199, ('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19, ('D', 'H'): 45,
('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31, ('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'):
106, ('E', 'D'): 25, ('E', 'E'): 0},['H', 'B', 'E', 'A', 'C', 'D', 'H']))

print(ruteo({('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241,
('A', 'H'):127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41,
('B', 'H'): 153, ('B', 'A'): 252, ('B','B'): 555, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269,
('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0,('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180,
('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'):194, ('D', 'F'): 109,
('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119,
('F','H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0},['H', 'B', 'D', 'A', 'F', 'C', 'E', 'H']))

print(ruteo({('BOG', 'BOG'): 0, ('BOG', 'MDE'): 21, ('BOG', 'PEI'): 57, ('BOG', 'SMR'): 58, ('BOG', 'CTG'): 195, ('MDE',
'BOG'): 127, ('MDE', 'MDE'): 0, ('MDE', 'PEI'): 231, ('MDE', 'SMR'): 113, ('MDE', 'CTG'): 254, ('PEI', 'BOG'): 153, ('PEI',
'MDE'): 252, ('PEI', 'PEI'): 0, ('PEI', 'SMR'): 56, ('PEI', 'CTG'): 126, ('SMR', 'BOG'): 196, ('SMR', 'MDE'): 128, ('SMR',
'PEI'): 80, ('SMR', 'SMR'): 0, ('SMR', 'CTG'): 136, ('CTG', 'BOG'): 30, ('CTG', 'MDE'): 40, ('CTG', 'PEI'): 256, ('CTG',
'SMR'): 121, ('CTG', 'CTG'): 0},['MDE', 'PEI', 'BOG', 'CTG', 'SMR', 'MDE']))

# EXPECTED
# {'ruta': 'H-A-F-B-D-C-E-H', 'distancia': 458}
# {'ruta': 'H-D-A-B-C-E-H', 'distancia': 393}
# Por favor revisar los datos de entrada.
# {'ruta': 'MDE-SMR-PEI-CTG-BOG-MDE', 'distancia': 370}
