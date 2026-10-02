from colorama import Fore, Style
from operaciones import (
    crear_matriz,
    sumar_matrices,
    restar_matrices,
    multiplicar_matrices,
    convertir_a_identidad,
)


def mostrar_menu():
    print("=== OPERACIONES CON MATRICES ===")
    print("1. Sumar matrices")
    print("2. Restar matrices")
    print("3. Multiplicar matrices")
    print("4. Convertir a matriz identidad")
    print("Escriba 'exit' para salir")
    print("===============================")


def ejecutar_opcion(opcion):
    if opcion == "1":
        filas = int(input("Filas: "))
        columnas = int(input("Columnas: "))
        print("Matriz A:")
        A = crear_matriz(filas, columnas)
        print("Matriz B:")
        B = crear_matriz(filas, columnas)
        print("Resultado:", sumar_matrices(A, B))
        return "valida"
    elif opcion == "2":
        filas = int(input("Filas: "))
        columnas = int(input("Columnas: "))
        print("Matriz A:")
        A = crear_matriz(filas, columnas)
        print("Matriz B:")
        B = crear_matriz(filas, columnas)
        print("Resultado:", restar_matrices(A, B))
        return "valida"
    elif opcion == "3":
        filasA = int(input("Filas matriz A: "))
        columnasA = int(input("Columnas matriz A: "))
        filasB = int(input("Filas matriz B: "))
        columnasB = int(input("Columnas matriz B: "))
        print("Matriz A:")
        A = crear_matriz(filasA, columnasA)
        print("Matriz B:")
        B = crear_matriz(filasB, columnasB)
        resultado = multiplicar_matrices(A, B)
        if resultado:
            print("Resultado:", resultado)
        return "valida"
    elif opcion == "4":
        filas = int(input("Filas: "))
        columnas = int(input("Columnas: "))
        print("Matriz A:")
        convertir_a_identidad(filas, columnas)
        return "valida"
    else:
        print("Opción inválida.")
        return "invalida"
