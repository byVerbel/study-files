# Calculadora para elementos geométricos de las secciones más comunes

from math import sin, sqrt, radians, cos, pi
# from sympy import acot
from mpmath import acot

# Pediré al usuario que ingrese la sección que desea calcular
# El programa pedirá los valores base de cada sección, estos pueden ser:
#       B, y, m, do, 0, k, r
# El programa retornará los valores: A, P, Rh, T, D, Z, ycg

print('''En este programa podrá calcular los elementos geométricos de secciones:
- Rectangular
- Triangular
- Trapecial
- Circular
- Parabólica
- Rectangular redondeada
- Triangular redondeada
''')
seccion = input('Tipo de sección: ')

# Función que verifica que los datos ingresados sean números
def checkfloat(n):
    try:
        n = float(n)
        return n
    except:
        print('Por favor digite un número.')
        quit()

# Defino todas las variables como funciones
def B():
    global b
    b = input('Ingresar base (B): ')
    b = checkfloat(b)
def y():
    global y
    y = input('Ingresar profundidad de flujo (y): ')
    y = checkfloat(y)
def m():
    global m
    m = input('Ingresar m (m): ')
    m = checkfloat(m)
def do():
    global do
    do = input('Ingresar diámetro (do): ')
    do = checkfloat(do)
def teta():
    global teta
    teta = input('Ingresar ángulo teta en radianes (0): ')
    if teta == 'pi':
        teta = pi
    teta = checkfloat(teta)
def k():
    global k
    k = input('Ingresar k (k): ')
    k = checkfloat(y)
def r():
    global r
    r = input('Ingresar radio: ')
    r = checkfloat(r)

# Función que me imprime los elementos geométricos
def elem(A,P,Rh,T,D,Z,ycg):
    print()
    print('Área mojada (A):', round(A,6))
    print('Perímetro mojado (P):', round(P,6))
    print('Radio hidráulico:', round(Rh,6))
    print('Ancho superficial:', round(T,6))
    print('Profundidad hidráulica:', round(D,6))
    print('Factor de sección:', round(Z,6))
    if seccion == 'Rectangular redondeada' or seccion == 'Triangular redondeada':
        print('No tenemos cálculo de profundidad centroidal.')
    else:
        print('Profundidad centroidal:', round(ycg,6))

# Defino función para seccion Rectangular, Trapecial y Triangular ya que son parecidas:
def rtt(b,m,y):
    # b = float(b); m = float(m); y = float(y)
    global A,P,T,ycg
    A = (b+m*y)*y
    P = b+(2*y*sqrt(1+m**2))
    T = b+2*m*y
    ycg= (((m*y**3)/3)+((b*y**2)/2))/A

# Defino función que calcula Rh, D y Z (ya que estos dependen de A, P y T).
# También imprime todos los resultados:
def RhDZ(A,P,T):
    global Rh,D,Z
    Rh = A/P
    D = A/T
    Z = pow(A,1.5)/sqrt(T)
    elem(A,P,Rh,T,D,Z,ycg)

# Calculo cada uno de los elementos geométricos de las secciones
if seccion == 'Trapecial':
    B(); m(); y()
    rtt(b,m,y)
    RhDZ(A,P,T)
elif seccion == 'Rectangular':
    B(); m = 0; y()
    rtt(b,m,y)
    RhDZ(A,P,T)
elif seccion == 'Triangular':
    b = 0; m(); y()
    rtt(b,m,y)
    RhDZ(A,P,T)
elif seccion == 'Circular':
    do(); teta(); y()
    A = 0.125*(teta-sin(teta))*do**2
    P = 0.5*teta*do
    if teta < pi:
        T = sin(teta/2)*do
    elif teta > pi:
        T = sin((2*pi-teta)/2)*do
    elif teta == pi:
        T = do
    ycg = y-(do/2)+(pow(T,3)/(12*A))
    RhDZ(A,P,T)
elif seccion == 'Parabólica':
    y(); k()
    A = (4/3)*sqrt(pow(y,3)/k)
    T = 2*sqrt(y/k)
    P = T+(8/3)*(pow(y,2)/T)
    ycg = (2/5)*y
    RhDZ(A,P,T)
elif seccion == 'Rectangular redondeada':
    B(); y(); r()
    A = (pi/2-2)*r**2 + (b+2*r)*y
    P = (pi-2)*r + b + 2*y
    T = b+2*r
    ycg = 0
    RhDZ(A,P,T)
elif seccion == 'Triangular redondeada':
    y(), m(), r()
    A = (pow(T,2)/(4*m)) - (r**2/m)*(1-m*acot(m))
    T = 2*(m*(y-r) + r*sqrt(1+m**2))
    P = (T/m)*sqrt(1+m**2) - (2*r/m)*(1-m*acot(m))
    ycg = 0
    RhDZ(A,P,T)
else:
    print('Por favor ingrese una sección válida.')
