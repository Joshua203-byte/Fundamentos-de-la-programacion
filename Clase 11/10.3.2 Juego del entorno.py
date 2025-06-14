'''
Clase:        10
Tema:         Matrices y listas
Ejercicio:    Juego del entorno
Descripción:  Dada una matriz binaria ingresada por el usuario, verifica para cada celda de una matriz binaria cuántos elementos con valor 
de 1 hay en las celdas vecinas (arriba, abajo,
izquierda, derecha, diagonales).

Autor:        Joshua Garcilazo
Fecha:        2025-06-14
Estado:       [   Terminado]
'''
N = int(input())
M = int(input())

matriz = []
for i in range(N):
    raw_input = input()
    temp_list = list(map(int, raw_input.split(",")))
    matriz.append(temp_list)

resultado = []

for i in range(N):
    fila_resultado = []
    for j in range(M):
        conteo = 0
        if i > 0 and j > 0 and matriz[i-1][j-1] == 1:
            conteo += 1
        if i > 0 and matriz[i-1][j] == 1:
            conteo += 1
        if i > 0 and j < M-1 and matriz[i-1][j+1] == 1:
            conteo += 1
        if j > 0 and matriz[i][j-1] == 1:
            conteo += 1
        if j < M-1 and matriz[i][j+1] == 1:
            conteo += 1
        if i < N-1 and j > 0 and matriz[i+1][j-1] == 1:
            conteo += 1
        if i < N-1 and matriz[i+1][j] == 1:
            conteo += 1
        if i < N-1 and j < M-1 and matriz[i+1][j+1] == 1:
            conteo += 1
        fila_resultado.append(conteo)
    resultado.append(fila_resultado)

for fila in resultado:
    print(fila)
