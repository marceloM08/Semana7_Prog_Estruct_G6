#multiplicaicon de matrices cuadradas
matrizA = []
matrizB = []
matrizC = []

#Matriz_1

print("Ingrese los valores de la matriz_1: ")

for fila in range(2):
    matrizA.append([])
    for colum in range(2):
        valor = (float-(input(f"fila {fila+1}, {colum+1}: ")))
        matrizA[fila].append(valor)
for fila in matrizA:
    print(fila)

#Matriz_2

print("Ingrese los valores de la matriz_2: ")

for fila in range(2):
    matrizB.append([])
    for colum in range(2):
        valor = (float(input(f"fila {fila+1}, {colum+1}: ")))
        matrizB[fila].append(valor)
for fila in matrizB:
    print(fila)

#Multipliacion

for i in range(len(matrizA)):
    matrizC.append([])
    for j in range(len(matrizA)):
        matrizC[i].append(matrizA[i][j] *  matrizB[i][j])

print("La multipliacion de estas matrices resulta en:  ")
for fila in matrizC:
    print(fila)