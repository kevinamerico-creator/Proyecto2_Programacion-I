"""Modulo de juego: modo manual y resolucion automatica."""

import time

from tableros import NIVELES
from logica import (crear_tablero, mostrar_tablero, mover_vehiculo, gano,
                    resolver, aplicar_movimiento, obtener_celdas,
                    NOMBRE_DIRECCION)
from historial import registrar_partida


def leer_opcion(mensaje, validas):
    """Pide un numero entero positivo hasta que sea una opcion valida."""
    while True:
        texto = input(mensaje).strip()
        if texto.isdigit() and int(texto) in validas:
            return int(texto)
        print("Opcion invalida. Ingrese un numero entero positivo del menu.")


def pedir_nombre():
    """Pide el nombre del jugador (no puede estar vacio)."""
    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if nombre != "":
            return nombre.replace(",", " ")
        print("El nombre no puede estar vacio.")


def pedir_pasos():
    """Pide cuantos espacios mover: un numero positivo o "todos"."""
    while True:
        texto = input("Mover cuantos espacios (1/2/todos): ").strip().lower()
        if texto == "todos":
            return "todos"
        if texto.isdigit() and int(texto) > 0:
            return int(texto)
        print("Error: ingrese un numero entero positivo o 'todos'.")


def jugar_nivel(tablero):
    """Juega un nivel. Devuelve (completado, movimientos).
    Si el jugador escribe Q, abandona y completado es False."""
    movimientos = 0
    while not gano(tablero):
        letra = input("Seleccione auto (Q para abandonar): ").strip().upper()
        if letra == "Q":
            return False, movimientos
        if len(letra) != 1 or not letra.isalpha() or len(obtener_celdas(tablero, letra)) == 0:
            print("Error: ese vehiculo no existe. Ingrese una letra del tablero.")
            continue

        direccion = input("Mover (U/D/L/R): ").strip().upper()
        if direccion not in ["U", "D", "L", "R"]:
            print("Error: direccion invalida. Use U, D, L o R.")
            continue

        pasos = pedir_pasos()
        exito, mensaje = mover_vehiculo(tablero, letra, direccion, pasos)
        if exito:
            movimientos = movimientos + 1
            mostrar_tablero(tablero)
        else:
            print(mensaje)
    return True, movimientos


def jugar_manual():
    """Modo manual: primero el Nivel 1 y luego el Nivel 2."""
    nombre = pedir_nombre()
    total = 0
    nivel_alcanzado = 1
    resultado = "Abandono"

    for i in range(len(NIVELES)):
        numero = i + 1
        nivel_alcanzado = numero
        print("\nCargando nivel " + str(numero) + "...")
        tablero = crear_tablero(NIVELES[i])
        mostrar_tablero(tablero)

        completado, movs = jugar_nivel(tablero)
        total = total + movs
        if not completado:
            print("Partida abandonada.")
            break
        print("Auto liberado. Nivel completado.")
        if numero == len(NIVELES):
            resultado = "Gano"
            print("Felicidades " + nombre + ", has ganado el juego!")

    registrar_partida(nombre, nivel_alcanzado, total, "Manual", resultado)


def jugar_automatico():
    """Resuelve los niveles solo, mostrando cada movimiento."""
    nombre = pedir_nombre()
    total = 0
    nivel_alcanzado = 1
    resultado = "Gano"

    for i in range(len(NIVELES)):
        numero = i + 1
        nivel_alcanzado = numero
        print("\nCargando nivel " + str(numero) + "...")
        tablero = crear_tablero(NIVELES[i])
        mostrar_tablero(tablero)

        print("\nResolviendo automaticamente...")
        solucion = resolver(tablero)
        if solucion is None:
            print("Este nivel no tiene solucion.")
            resultado = "Abandono"
            break

        numero_mov = 0
        for letra, direccion, pasos in solucion:
            numero_mov = numero_mov + 1
            time.sleep(0.5)
            texto = "Movimiento " + str(numero_mov) + ": mover " + letra + " hacia " + NOMBRE_DIRECCION[direccion]
            if pasos > 1:
                texto = texto + " (" + str(pasos) + " espacios)"
            print(texto)
            aplicar_movimiento(tablero, letra, direccion, pasos)
            mostrar_tablero(tablero)
        total = total + len(solucion)
        print("Auto liberado. Nivel completado.")

    registrar_partida(nombre, nivel_alcanzado, total, "Automatico", resultado)
