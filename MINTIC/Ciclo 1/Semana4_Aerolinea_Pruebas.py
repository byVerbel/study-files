import Semana4_Aerolinea

vuelosEjemplo = [{"aerolinea": "AVIANCA", 'codigo': "AHF21", "origen": "BOG", "destino": "CTG", "distancia": 295, "retraso": 5, "duracion": 120, "salida":600},
                 {"aerolinea": "VIVAAIR", 'codigo': "VVE01", "origen": "BOG", "destino": "CTG", "distancia": 295, "retraso": 2, "duracion": 115, "salida":555},
                 {"aerolinea": "AVIANCA", 'codigo': "AHF21", "origen": "CTG", "destino": "BOG", "distancia": 295, "retraso": 15, "duracion": 120, "salida":830},
                 {"aerolinea": "VIVAAIR", 'codigo': "VVE01", "origen": "CTG", "destino": "PEI", "distancia": 325, "retraso": 5, "duracion": 135, "salida":800},
                 {"aerolinea": "AVIANCA", 'codigo': "AHF23", "origen": "BOG", "destino": "CLO", "distancia": 255, "retraso": 25, "duracion": 170, "salida":605},
                 {"aerolinea": "VIVAAIR", 'codigo': "VVE01", "origen": "PEI", "destino": "BOG", "distancia": 220, "retraso": 5, "duracion": 60, "salida":1030},
                 {"aerolinea": "AVIANCA", 'codigo': "AHF23", "origen": "CLO", "destino": "CTG", "distancia": 400, "retraso": 20, "duracion": 160, "salida":1200}]

print(Semana4_Aerolinea.aerolinea_con_vuelos(vuelosEjemplo))
print(Semana4_Aerolinea.avion_con_vuelos(vuelosEjemplo))
print(Semana4_Aerolinea.ciudad_con_vuelos(vuelosEjemplo))
