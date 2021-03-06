# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:02:19 2020

@author: Julian
"""

import numpy as np

def Triqui():
    
    jugando = True
    tablero = np.zeros((3,3))
    simbolo = {0 : '_',
               1 : 'X',
               -1 : 'O'}
    
    jugador = 1
    turno = 0
    
    while jugando:
        
        # Pintar el tablero
        for fila in range(3):
            print('|',end='')
            for columna in range(3):
                print (simbolo[tablero[fila][columna]],'|' , sep='', end='')
            print('\n', end='')
                    
        # Preguntar jugada
        try:
            i, j = input('Por favor ingrese una posicion \n').split(',')
            i, j = int(i) -1, int(j) -1
            valida = True
        except:
            print('Ingrese una jugada valida!')
            valida = False
            
        if i > 2 or i < 0 or j > 2 or j < 0:
            valida = False
        
        # Verificar que la jugada sea legal (que no esta ocupada la casilla)
        if valida and tablero[i][j] == 0:
        
            # Actualizar el tablero
            tablero[i][j] = jugador
            
            # Aumentar el turno
            turno += 1
            
            # Verificar ganador
            
            '''
            if sum(tablero[0,:]) == 3 or sum(tablero[0,:]) == -3: # Fila 1
                jugando = False
            elif sum(tablero[1,:]) == 3 or sum(tablero[1,:]) == -3: # Fila 2
                jugando = False
            elif sum(tablero[2,:]) == 3 or sum(tablero[2,:]) == -3: # Fila 3
                jugando = False
            elif sum(tablero[:,0]) == 3 or sum(tablero[:,0]) == -3: # Columna 1
                jugando = False
            elif sum(tablero[:,1]) == 3 or sum(tablero[:,1]) == -3: # Columna 2
                jugando = False
            elif sum(tablero[:,2]) == 3 or sum(tablero[:,2]) == -3: # Columna 1
                jugando = False
            '''
            
            for linea in range(3):
                if sum(tablero[linea,:]) == 3 or sum(tablero[linea,:]) == -3: # Filas
                    jugando = False
                if sum(tablero[:,linea]) == 3 or sum(tablero[:,linea]) == -3: # Columnas
                    jugando = False
            
            if sum(tablero.diagonal()) == 3 or sum(tablero.diagonal()) == -3: # Columna 1
                jugando = False
            elif sum(np.fliplr(tablero).diagonal()) == 3 or sum(np.fliplr(tablero).diagonal()) == -3:            
                jugando = False
                
            # Verificar empaate
            if turno == 9 and jugando:
                print('Empate!')
                jugando = False
            elif not jugando:
                print('Gano el jugador '+ simbolo[jugador] + ', felicidades!')
        
            # Cambiar de turno
            jugador = jugador * (-1)
            
        
        else:
            print('Jugada invalida! por favor selecciona una casilla vacia')
    
    # Pintar el tablero final
    for fila in range(3):
            print('|',end='')
            for columna in range(3):
                print (simbolo[tablero[fila][columna]],'|' , sep='', end='')
            print('\n', end='')
    
    print('Gracias por jugar!')
    
Triqui()
    
    