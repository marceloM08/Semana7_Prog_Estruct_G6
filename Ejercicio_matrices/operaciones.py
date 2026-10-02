from colorama import Fore, Style

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    valor = float(input(f"({i+1},{j+1}): "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Error: dígito inválido.")
        matriz.append(fila)
    return matriz

def sumar_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def restar_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiplicar_matrices(A, B):
    if len(A[0]) != len(B):
        print("Error: dimensiones incompatibles.")
        return
    resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                resultado[i][j] += A[i][k] * B[k][j]
    return resultado

def convertir_a_identidad(filas, columnas):
    while True:
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                while True:
                    try:
                        valor = float(input(f"({i+1},{j+1}): "))
                        fila.append(valor)
                        break
                    except ValueError:
                        print("Error: dígito inválido.")
            matriz.append(fila)

        print("\nLa matriz ingresada es:")
        for fila in matriz:
            print(" ".join(str(x) for x in fila))

        cambiar = input("\n¿Desea cambiar los datos ingresados? (sí/no): ").lower()
        if cambiar == "si":
            print("\nIngrese nuevamente los valores...")
            continue
        else:
            break

    identidad = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(1 if i == j else 0)
        identidad.append(fila)

    print("\nLa matriz de identidad es:")
    for i in range(filas):
        for j in range(columnas):
            if i == j:
                print(Fore.BLUE + str(identidad[i][j]) + Style.RESET_ALL, end=" ")
            else:
                print(identidad[i][j], end=" ")
        print()

    return identidad