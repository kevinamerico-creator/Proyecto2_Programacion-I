

print("""==========DESATASCA EL AUTO - MENU PRINCIPAL ==========
          1. Iniciar nuevo juego
          2. Resolver automaticamente 
          3. Ver historial de juegos
          4. Salir
=========================================================""")
print()

while True:
    opcion = int(input("Seleccione una opcion: "))
    if opcion in range(1, 5):
        break
nivel_1 = ["########",
           "#AB CFG#",
           ]
def IniciarJuego():
    print("Cargando nivel 1...")

