from juego import jugar_manual, jugar_automatico, leer_opcion
from historial import mostrar_historial


def mostrar_menu():
    """Imprime el menu principal."""
    print("\n===== DESATASCA EL AUTO - MENU PRINCIPAL =====")
    print("1. Iniciar nuevo juego")
    print("2. Resolver automaticamente")
    print("3. Ver historial de juegos")
    print("4. Salir")
    print("==============================================")


def main():
    while True:
        mostrar_menu()
        opcion = leer_opcion("Ingrese una opcion: ", (1, 2, 3, 4))
        if opcion == 1:
            jugar_manual()
        elif opcion == 2:
            jugar_automatico()
        elif opcion == 3:
            mostrar_historial()
        else:
            print("Hasta pronto!")
            break


if __name__ == "__main__":
    main()
