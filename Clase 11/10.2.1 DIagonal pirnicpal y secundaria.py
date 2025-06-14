
'''
Clase:        10
Tema:         Matrices y listas
Ejercicio:    Diagonal principal y secundaria
Descripción:  Dada una matriz cuadrada ingresada por el
usuario, crea dos listas, una con los
elementos de la diagonal principal y la otra
con los elementos de la diagonal
secundaria.

Autor:        Joshua Garcilazo
Fecha:        2025-06-14
Estado:       [   Terminado]
'''
N = int(input())
matriz = []
for _ in range(N):
    fila = list(map(int, input().split(',')))
    matriz.append(fila)

diagonal_principal = [matriz[i][i] for i in range(N)]
diagonal_secundaria = [matriz[i][N - 1 - i] for i in range(N)]

print("Salida")
print(diagonal_principal)
print(diagonal_secundaria)
