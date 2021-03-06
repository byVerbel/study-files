def aerolinea_con_vuelos(vuelos: list)-> tuple:
    aerolineas = {}
    tuplas = []
    for vuelo in vuelos:
        aerolineas[vuelo['aerolinea']] = aerolineas.get(vuelo['aerolinea'],0)+1
    for empresa in aerolineas:
        tuplas.append((aerolineas[empresa], empresa))
        tupla = max(tuplas)
    salida = (tupla[1], tupla[0])
    return salida

def avion_con_vuelos(vuelos: list)-> tuple:
    aviones = {}
    tuplas = []
    for vuelo in vuelos:
        aviones[vuelo['codigo']] = aviones.get(vuelo['codigo'],0)+1
    for avion in aviones:
        tuplas.append((aviones[avion], avion))
        tupla = max(tuplas)
    salida = (tupla[1], tupla[0])
    return salida

def ciudad_con_vuelos(vuelos: list)-> tuple:
    ciudades = {}
    tuplas = []
    for vuelo in vuelos:
        ciudades[vuelo['origen']] = ciudades.get(vuelo['origen'],0)+1
        ciudades[vuelo['destino']] = ciudades.get(vuelo['destino'],0)+1
    for ciudad in ciudades:
        tuplas.append((ciudades[ciudad], ciudad))
        tupla = max(tuplas)
    salida = (tupla[1], tupla[0])
    return salida
