from unicodedata import normalize

# Defino diccionario que reciba la información previamente describida
def promedio_facultades(info: dict, contando_externos : bool = True ) -> tuple:
    # Diccionario que contenga las facultades y tuplas(nota, creditos) para después validar
    facultades = {materia['facultad']: list() for estudiante in info.values() for materia in estudiante['materias'] }
    correos = list()
    negativos = { 'nm.cordoba54', 'pn.alvarez60', 'cj.sanchez71', 'cs.garcia72' }

    # Ciclo que recorra los items de info
    for codigo, estudiante in info.items():
        est_code = str(codigo)
        programa = estudiante['programa']
        # Creo correo del estudiante
        nombres = estudiante['nombres'].lower().split()
        nombre1 = normalize('NFKD', nombres[0]).encode("ascii","ignore").decode("ascii")
        apellidos = estudiante['apellidos'].replace(',', '')
        apellidos = apellidos.lower().split()
        apellido1 = normalize('NFKD', apellidos[0]).encode("ascii","ignore").decode("ascii")
        apellido2 = normalize('NFKD', apellidos[1]).encode("ascii","ignore").decode("ascii")
        documento = str(estudiante['documento'])
        if len(nombres)==2:
            nombre2 = normalize('NFKD', nombres[1]).encode("ascii","ignore").decode("ascii")
            correo = nombre1[0] + nombre2[0] + '.' + apellido2 + documento[-2:]
        else:
            correo = nombre1[0] + apellido2[0] + '.' + apellido1 + documento[-2:]

        # Ciclo que recorra las materias vistas por cada estudiante
        for materia in estudiante['materias']:
            code = materia['codigo'].split('-')[0]
            if materia['retirada'] == 'No':
                if contando_externos:
                    facultades[materia['facultad']].append((materia['nota'], materia['creditos']))
                    if correo not in correos and correo not in negativos:
                        correos.append(correo)
                else:
                    if code != programa or est_code[4:6] == '05':
                        pass
                    else:
                        facultades[materia['facultad']].append((materia['nota'], materia['creditos']))
                        if correo not in correos and correo not in negativos:
                            correos.append(correo)
    
    notas = dict()
    try:
        for facultad, tuplas in facultades.items():
            superior = 0
            inferior = 0
            for nota, credito in tuplas:
                superior += nota*credito
                inferior += credito
            promedio = superior/inferior
            facultades[facultad] = round(promedio, 2)
        for facultad in sorted(facultades):
            notas[facultad] = facultades[facultad]
        return (notas, sorted(correos))
    except:
        return 'Error numérico.'
