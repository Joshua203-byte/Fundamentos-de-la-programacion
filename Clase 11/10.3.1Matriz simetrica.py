'''
Clase:        10
Tema:         Matrices y listas
Ejercicio:     Matriz simétrica
Descripción:  Dada una matriz cuadrada ingresada por el
usuario, comprueba si la matriz cuadrada es
simétrica respecto a su diagonal principal.
Autor:        Joshua Garcilazo
Fecha:        2025-06-14
Estado:       [   Terminado]
'''
N = int(input())

matriz = []
for _ in range(N):
    while True:
        fila_str = input().strip()
        try:
            fila = list(map(int, fila_str.split(',')))
            if len(fila) != N:
                print(f"Error: Debes ingresar exactamente {N} números.")
            else:
                matriz.append(fila)
                break
        except ValueError:
            print("Error: Ingresa solo números separados por comas.")

es_simetrica = True
for i in range(N):
    for j in range(N):
        if matriz[i][j] != matriz[j][i]:
            es_simetrica = False
            break
    if not es_simetrica:
        break


if es_simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")

