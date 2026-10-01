"""
Dame una matriz cuadrada,
convertirla a matriz de identidad
"""

matrizA = []

for fila in range(2):
    matrizA.append([])
    for colum in range(2):
        valor = float(input(f"fila {fila+1}, {colum+1}: "))
        matrizA[fila].append(valor)

def convertir_identidad(matriz):
    l = len(matriz)
    for i in range(l):
        for j in range(l):
            if i == j:
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0
    return matriz

resultado = convertir_identidad(matrizA)
print(resultado)