from menu import mostrar_menu, ejecutar_opcion


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion.lower() == "exit":
            print("Saliendo del programa...")
            break

        resultado = ejecutar_opcion(opcion)

        if resultado != "invalida":
            continuar = input(
                "¿Desea continuar? (escriba 'exit' para salir, Enter para seguir): "
            )
            if continuar.lower() == "exit":
                print("Saliendo del programa...")
                break


if __name__ == "__main__":
    main()
