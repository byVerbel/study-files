def prestamo(informacion:dict)->dict:
    # Me facilitaré el uso de los datos
    idp = informacion['id_prestamo']
    casado = informacion['casado']
    depen = informacion['dependientes']
    educ = informacion['educacion']
    indepen = informacion['independiente']
    id = informacion['ingreso_deudor']
    ic = informacion['ingreso_codeudor']
    cp = informacion['cantidad_prestamo']
    pp = informacion['plazo_prestamo']
    hc = informacion['historia_credito']
    tp = informacion['tipo_propiedad']
    if hc==1:
        if ic>0 and id/9>cp:
            aprovado = True
        else:
            if (depen=='3+' or depen>2) and indepen=='Si':
                if ic/12>cp:
                    aprovado = True
                else:
                    aprovado = False
            else:
                if cp<200:
                    aprovado = True
                else:
                    aprovado = False
    else:
        if indepen=='Si':
            if not (casado=='Si' and (depen=='3+' or depen>1)):
                if id/10>cp and ic/10>cp:
                    if cp<180:
                        aprovado = True
                    else:
                        aprovado = False
                else:
                    aprovado = False
            else:
                aprovado = False
        else:
            if not tp=='Semiurbano' and (not depen == '3+' and depen<2):
                if educ=='Graduado':
                    if id/11>cp and ic/11>cp:
                        aprovado = True
                    else:
                        aprovado = False
                else:
                    aprovado = False
            else:
                aprovado = False
    resp = {'id_prestamo': idp, 'aprobado': aprovado}
    return resp

informacion = {}
informacion['id_prestamo'] = 'RETOS2_001'
informacion['casado'] = 'No'
informacion['dependientes'] = 1
informacion['educacion'] = 'Graduado'
informacion['independiente'] = 'Si'
informacion['ingreso_deudor'] = 4692
informacion['ingreso_codeudor'] = 0
informacion['cantidad_prestamo'] = 106
informacion['plazo_prestamo'] = 360
informacion['historia_credito'] = 1
informacion['tipo_propiedad'] = 'Rural'

print(prestamo(informacion))

informacion = {}
informacion['id_prestamo'] = 'RETOS2_002'
informacion['casado'] = 'No'
informacion['dependientes'] = '3+'
informacion['educacion'] = 'No Graduado'
informacion['independiente'] = 'No'
informacion['ingreso_deudor'] = 1830
informacion['ingreso_codeudor'] = 0
informacion['cantidad_prestamo'] = 100
informacion['plazo_prestamo'] = 360
informacion['historia_credito'] = 0
informacion['tipo_propiedad'] = 'Urbano'

print(prestamo(informacion))

informacion = {}
informacion['id_prestamo'] = 'RETOS2_003'
informacion['casado'] = 'No'
informacion['dependientes'] = 0
informacion['educacion'] = 'No Graduado'
informacion['independiente'] = 'No'
informacion['ingreso_deudor'] = 3748
informacion['ingreso_codeudor'] = 1668
informacion['cantidad_prestamo'] = 110
informacion['plazo_prestamo'] = 360
informacion['historia_credito'] = 1
informacion['tipo_propiedad'] = 'Semiurbano'

print(prestamo(informacion))
