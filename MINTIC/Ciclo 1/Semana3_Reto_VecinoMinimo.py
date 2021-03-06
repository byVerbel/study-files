def ruteonuevo (distancias: dict, ruta_inicial: list)-> dict:
    validacion(distancias)
    #preparar las variables de salida
    ruta_inicial=ruta_inicial[0:len(ruta_inicial)-1]
    rutaSolucion=[]
    kilometros = 0

    #modelar los nodos ya visitados
    yaesta = {}
    for nodo in ruta_inicial:
        yaesta.update({nodo:0})

    #inicializar el nodo de trabajo
    nodoActual = ruta_inicial[0]

    #iterar cuantos arcos debamos agregar
    for i in range(1,len(ruta_inicial)):

        #Crear unicamente las llaves que me interesan
        listallaves = []
        for nodo in ruta_inicial:
            if nodo != nodoActual and yaesta[nodo]==0:
                arco = (nodoActual,nodo)
                listallaves.append(arco)

        #Encontrar el minimo
        minimaDistancia = 999999
        for arco in listallaves:
            if distancias[arco] < minimaDistancia:
                minimaDistancia = distancias[arco]
                minimoarco = (minimaDistancia, arco)

        #Actualizar las listas de solucion y de YaEsta
        rutaSolucion.append(minimoarco[1])
        kilometros = kilometros + minimoarco[0]

        yaesta[minimoarco[1][0]]= 1
        yaesta[minimoarco[1][1]]= 1

        nodoActual = minimoarco[1][1]

    #tenemos que crear el ultimo
    ultimoarco = (nodoActual,ruta_inicial[0])
    rutaSolucion.append(ultimoarco)
    kilometros = kilometros + distancias[ultimoarco]

    #Dar la salida
    salida = {}
    salida.update({"ruta":rutaSolucion})
    salida.update({"distancia":kilometros})

    return salida



def ruteo (distancias: dict, ruta_inicial: list)-> dict:
    if validacion(distancias):
        return 'Por favor revisar los datos de entrada.'
        exit()
    distancia = []
    ruta = ['H']
    iteracion = {}
    actual = None
    # Hago un ciclo que no se cierre hasta tener mi nueva ruta
    while len(ruta) != len(ruta_inicial):
        # Condiciono que mi primera iteración comienza con 'H'
        if actual == None:
            actual = 'H'
        else:
            pass
        # Condiciono que mi último destino es 'H'
        if len(ruta)==len(ruta_inicial)-1:
            distancia.append(distancias[actual,'H'])
            ruta.append('H')
        else:
            # Recorro las llaves del diccionario
            for i,j in distancias.keys():
                # Encuentro las llaves que aplican en mi ruta y las agrego a otro diccionario temporal
                if i == actual and j != actual and j in ruta_inicial and j not in ruta:
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
    salida = {'ruta':ruta_final,'distancia':distancia_final}
    return salida
