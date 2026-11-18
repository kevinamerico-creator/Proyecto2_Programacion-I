from datetime import datetime

ARCHIVO = "historial.txt"
ENCABEZADOS = ["Nombre", "Fecha y hora", "Nivel", "Tipo", "Resul.", "Mov."]


def registrar_partida(nombre, nivel, movimientos, tipo, resultado):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    archivo = open(ARCHIVO, "a", encoding="utf-8")
    archivo.write(nombre + "," + fecha + "," + str(nivel) + "," + tipo + "," +
                  resultado + "," + str(movimientos) + "\n")
    archivo.close()


def cargar_historial():
    partidas = []
    try:
        archivo = open(ARCHIVO, "r", encoding="utf-8")
    except FileNotFoundError:
        return partidas              # todavia no hay partidas
    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            partidas.append(linea.split(","))
    archivo.close()
    return partidas


def imprimir_fila(valores, anchos):
    """Imprime una fila de la tabla con cada columna del ancho indicado."""
    texto = "|"
    for i in range(len(valores)):
        texto = texto + " " + valores[i].ljust(anchos[i]) + " |"
    print(texto)


def mostrar_historial():
    """Muestra todas las partidas en formato de tabla."""
    partidas = cargar_historial()
    print("\n===== HISTORIAL DE JUEGOS =====")
    if len(partidas) == 0:
        print("Aun no hay partidas registradas.")
        return

    anchos = []
    for encabezado in ENCABEZADOS:
        anchos.append(len(encabezado))
    for partida in partidas:
        for i in range(len(partida)):
            if len(partida[i]) > anchos[i]:
                anchos[i] = len(partida[i])

    guiones = []
    for ancho in anchos:
        guiones.append("-" * ancho)

    imprimir_fila(ENCABEZADOS, anchos)
    imprimir_fila(guiones, anchos)
    for partida in partidas:
        imprimir_fila(partida, anchos)
