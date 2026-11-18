"""Modulo de logica: reglas del tablero, movimientos y resolucion automatica."""

# Cuanto cambia (fila, columna) al mover en cada direccion
DIRECCIONES = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

# Texto para mostrar: "mover E hacia la izquierda"
NOMBRE_DIRECCION = {"U": "arriba", "D": "abajo",
                    "L": "la izquierda", "R": "la derecha"}


def crear_tablero(filas):
    """Convierte la lista de textos en una matriz (lista de listas)."""
    tablero = []
    for fila in filas:
        tablero.append(list(fila))
    return tablero


def copiar_tablero(tablero):
    """Devuelve una copia del tablero para no modificar el original."""
    copia = []
    for fila in tablero:
        copia.append(fila[:])
    return copia


def tablero_a_texto(tablero):
    """Une todo el tablero en un solo texto (sirve para comparar tableros)."""
    texto = ""
    for fila in tablero:
        texto = texto + "".join(fila)
    return texto


def mostrar_tablero(tablero):
    """Imprime el tablero en pantalla."""
    for fila in tablero:
        print("".join(fila))


def obtener_celdas(tablero, letra):
    """Devuelve la lista de posiciones (fila, columna) que ocupa un vehiculo."""
    celdas = []
    for f in range(len(tablero)):
        for c in range(len(tablero[f])):
            if tablero[f][c] == letra:
                celdas.append((f, c))
    return celdas


def es_horizontal(celdas):
    """True si el vehiculo esta en una sola fila (horizontal)."""
    return celdas[0][0] == celdas[-1][0]


def pasos_maximos(tablero, letra, direccion):
    """Cuenta cuantos espacios libres tiene el vehiculo en esa direccion."""
    celdas = obtener_celdas(tablero, letra)
    cambio_fila = DIRECCIONES[direccion][0]
    cambio_col = DIRECCIONES[direccion][1]

    # Celda de adelante: la primera si va arriba/izquierda, la ultima si no
    if direccion == "U" or direccion == "L":
        fila, col = celdas[0]
    else:
        fila, col = celdas[-1]

    pasos = 0
    while True:
        fila = fila + cambio_fila
        col = col + cambio_col
        fuera = fila < 0 or fila >= len(tablero) or col < 0 or col >= len(tablero[0])
        if fuera or tablero[fila][col] != " ":
            break
        pasos = pasos + 1
    return pasos


def aplicar_movimiento(tablero, letra, direccion, pasos):
    """Mueve el vehiculo (se asume que el movimiento ya es valido)."""
    celdas = obtener_celdas(tablero, letra)
    cambio_fila = DIRECCIONES[direccion][0] * pasos
    cambio_col = DIRECCIONES[direccion][1] * pasos

    for fila, col in celdas:           # 1) borrar el vehiculo
        tablero[fila][col] = " "
    for fila, col in celdas:           # 2) dibujarlo en la nueva posicion
        tablero[fila + cambio_fila][col + cambio_col] = letra


def mover_vehiculo(tablero, letra, direccion, pasos):
    """Valida y realiza un movimiento. 'pasos' es un numero o "todos".
    Devuelve (exito, mensaje)."""
    celdas = obtener_celdas(tablero, letra)
    if letra == "#" or len(celdas) == 0:
        return False, "Error: el vehiculo '" + letra + "' no existe en el tablero."

    # Un vehiculo horizontal solo se mueve L/R y uno vertical solo U/D
    if es_horizontal(celdas) and (direccion == "U" or direccion == "D"):
        return False, "Error: " + letra + " es horizontal, solo se mueve con L o R."
    if not es_horizontal(celdas) and (direccion == "L" or direccion == "R"):
        return False, "Error: " + letra + " es vertical, solo se mueve con U o D."

    maximo = pasos_maximos(tablero, letra, direccion)
    if maximo == 0:
        return False, "Error: movimiento invalido, hay un muro u otro vehiculo en el camino."
    if pasos == "todos":
        pasos = maximo
    if pasos > maximo:
        return False, "Error: " + letra + " solo puede avanzar " + str(maximo) + " espacio(s) en esa direccion."

    aplicar_movimiento(tablero, letra, direccion, pasos)
    return True, "Movimiento realizado."


def gano(tablero):
    """True si X llego a la ultima columna (la salida)."""
    for fila, col in obtener_celdas(tablero, "X"):
        if col == len(tablero[0]) - 1:
            return True
    return False


def resolver(tablero):
    """Resuelve el tablero probando todos los movimientos posibles, nivel por
    nivel (busqueda en anchura). Devuelve la lista de movimientos
    [(letra, direccion, pasos), ...] o None si no hay solucion."""

    # Lista de vehiculos que hay en el tablero
    letras = []
    for fila in tablero:
        for valor in fila:
            if valor.isalpha() and valor not in letras:
                letras.append(valor)

    visitados = [tablero_a_texto(tablero)]   # tableros ya revisados
    cola = [(tablero, [])]                   # pendientes: (tablero, movimientos)

    while len(cola) > 0:
        actual, camino = cola.pop(0)         # sacamos el primero de la cola
        if gano(actual):
            return camino

        for letra in letras:
            if es_horizontal(obtener_celdas(actual, letra)):
                direcciones = ["L", "R"]
            else:
                direcciones = ["U", "D"]

            for direccion in direcciones:
                for pasos in range(1, pasos_maximos(actual, letra, direccion) + 1):
                    nuevo = copiar_tablero(actual)
                    aplicar_movimiento(nuevo, letra, direccion, pasos)
                    texto = tablero_a_texto(nuevo)
                    if texto not in visitados:
                        visitados.append(texto)
                        cola.append((nuevo, camino + [(letra, direccion, pasos)]))
    return None
