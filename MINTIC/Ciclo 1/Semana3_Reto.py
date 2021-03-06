# Defino funcion para validar distancias positivas en el diccionario
def validacion(distancias: dict):
    close = None
    # Con este ciclo encuentro las tuplas de nodos
    for i, j in distancias.keys():
        # Condiciono que todas las tuplas tengan distancia mayor a 0
        if distancias[i, j] < 0:
            close = True
        # Condiciono que las tuplas del mismo nodo tengan distancia 0
        elif i == j and distancias[i, j] != 0:
            close = True
        else:
            pass
    return close


# Defino función que encuentra distancia de la ruta_inicial
def ruteo_inicial(distancias: dict, ruta_inicial: list)-> int:
    # Defino 2 listas en las que agrego las tuplas de nodos y sus distancias
    tuplas = list()
    distancias_tuplas = list()
    # Con este ciclo encuentro las tuplas de mi ruta_inicial
    for nodo in range(len(ruta_inicial)-1):
        tuplas.append((ruta_inicial[nodo], ruta_inicial[nodo+1]))
    # Con este ciclo encuentro las distancias de mis tuplas
    for tupla in tuplas:
        distancias_tuplas.append(distancias[tupla])

    distancia_inicial = sum(distancias_tuplas)
    return distancia_inicial


# Defino función que encuentre una ruta óptima
def ruteo(distancias: dict, ruta_inicial: list)-> dict:
    # Primero tengo que validar
    if validacion(distancias):
        return 'Por favor revisar los datos de entrada.'
        exit()

    # Encuentro la distancia de la ruta_inicial. Sería mi ruta solución en ruteos de mínimo 3 nodos
    distancia_solucion = ruteo_inicial(distancias, ruta_inicial)
    ruta_solucion = ruta_inicial.copy()

    # Defino algunas variables antes de entrar a los ciclos
    tuplas = list()
    ruta_actual = list()
    mejoro = True

    # Con este ciclo veo si mi condición mejora al iterar
    while mejoro:
        # Defino algunas variables y establezco mejoro como Falsa
        mejoro = False
        ruta_actual = ruta_solucion.copy()
        ruta_iteracion = ruta_actual.copy()
        distancias_tuplas = list()

        # Con este ciclo recorro los nodos i
        for i in range(1, len(ruta_actual)-1):
            # Con este ciclo recorro los nodos j para el intercambio
            for j in range(i+1, len(ruta_actual)-1):
                # Aquí hago el intercambio de nodos
                ruta_iteracion[i], ruta_iteracion[j] = ruta_iteracion[j], ruta_iteracion[i]

                # Aquí encuentro las tuplas de mi iteración
                for nodo in range(len(ruta_iteracion)-1):
                    tuplas.append((ruta_iteracion[nodo], ruta_iteracion[nodo+1]))

                # Aquí encuentro las distancias entre los nodos y las ingreso en una lista
                for tupla in tuplas:
                    distancias_tuplas.append(distancias[tupla])

                # Aquí compruebo si mi iteración es más corta que la mejor ruta hasta el momento
                if sum(distancias_tuplas) < distancia_solucion:
                    distancia_solucion = sum(distancias_tuplas)
                    ruta_solucion = ruta_iteracion.copy()
                    mejoro = True
                else:
                    pass

                # Reinicio distintas variables para la siguiente iteración
                ruta_iteracion = ruta_actual.copy()
                tuplas.clear()
                distancias_tuplas.clear()

    # Aquí defino el retorno
    ruta_final = '-'.join(ruta_solucion)
    salida = {'ruta': ruta_final, 'distancia': distancia_solucion}
    return salida
