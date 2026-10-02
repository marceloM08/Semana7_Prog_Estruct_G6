"""
Dada una Matriz de Identidad nxm
mostrar en color azul diagonal de 1
"""

from colorama import Fore, Style

filas = int(input("Filas: "))
columnas = int(input("Columnas: "))

matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(1 if i == j else 0)
    matriz.append(fila)

print("La matriz de identidad es:")
for i in range(filas):
    for j in range(columnas):
        if i == j:
            print(Fore.BLUE + str(matriz[i][j]) + Style.RESET_ALL, end=" ")
        else:
            print(matriz[i][j], end=" ")
    print()
