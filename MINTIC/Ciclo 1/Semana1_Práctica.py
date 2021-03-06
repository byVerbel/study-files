# Realize un programa que sume solamente los decimales de un número

def decimalsum(A,B):
    # A = input('Please enter first number: ')
    # B = input('Please enter second number: ')
    A = float(A)-int(float(A))
    B = float(B)-int(float(B))
    print(A+B)
    # print(round(A+B,6))

# -----------------------------------------------------------------------------------------------------------------

# Programa que determine a qué hora se debe iniciar un experimento (como máximo)
# si te dicen la duración del experimento y el tiempo en el que finalizan las entregas.

def inicio_reaccion(codigo,hora_terminacion,minuto_terminacion,duracion_horas,duracion_minutos,duracion_segundos):
    cod = codigo
    if duracion_segundos>0:
        ss = 60-duracion_segundos
        duracion_minutos = duracion_minutos+1
    else:
        ss = 00
    mm = minuto_terminacion-duracion_minutos
    hh = hora_terminacion-duracion_horas
    print(f"La reacción {cod} debe iniciarse a las {hh} horas, {mm} minutos con {ss} segundos para que esté lista en el momento requerido.")

inicio_reaccion('HHA01',16,30,4,11,23)
inicio_reaccion('IQ200',16,30,7,24,58)
inicio_reaccion('IQ200',16,30,7,24,00)
