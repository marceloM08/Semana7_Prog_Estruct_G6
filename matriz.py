#Suma de matrices
""" Leer 2 matrices 3 x 3 y sumar es una matriz """
matriz1 = []
for fila in range(3):
    matriz1.append([])
    for colum in range(3):
        valor = (int(input(f"fila {fila+1}, {colum+1}: ")))
        matriz1[fila].append(valor)
for fila in matriz1:
    print(fila)

matriz2 = []
for fila in range(3):
    matriz2.append([])
    for colum in range(3):
        valor = (int(input(f"fila {fila+1}, {colum+1}: ")))
        matriz2[fila].append(valor)
for fila in matriz2:
    print(fila)


matriz3 = []
for i in range(len(matriz1)):
    matriz3.append([])
    for j in range(len(matriz1)):
        matriz3[i].append(matriz1[i][j] + matriz2[i][j])

print ("Sumatoria de las matrizes: ")
for fila in matriz3:
    print(fila)