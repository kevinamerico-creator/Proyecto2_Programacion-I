"""Modulo de tableros: define los niveles del juego.

Convenciones:
  '#'      -> muro
  ' '      -> espacio libre
  'A'..'Z' -> vehiculos (autos y camiones)
  'X'      -> vehiculo principal
La fila de X no tiene muro en la ultima columna: ahi esta la salida.
"""

NIVEL_1 = [
    "########",
    "#AB CFG#",
    "#AB CFG#",
    "#XX CFG ",   # <- fila de X, la salida esta al final (derecha)
    "#   EEE#",
    "#DD    #",
    "#      #",
    "########",
]

NIVEL_2 = [
    "########",
    "#AAB  C#",
    "#D BEEC#",
    "#DXX  C ",   # <- fila de X, la salida esta al final (derecha)
    "#DFFG  #",
    "#H  GII#",
    "#HJJJ  #",
    "########",
]

# Lista ordenada de niveles que se cargan uno tras otro
NIVELES = [NIVEL_1, NIVEL_2]
