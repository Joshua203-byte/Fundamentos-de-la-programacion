'''
Clase:        6
Tema:         Aprendiendo con listas
Ejercicio:    Eliminando valores duplicados de una lista
Descripción:  Eliminar los numeros duplicados de una lista y mostrar la lista resultante.

Autor:        Joshua Garcilazo
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

numeros = list(map(int, input().split(' ')))
numeros_sin_repetidos = []
for num in numeros:
    if num not in numeros_sin_repetidos:
        numeros_sin_repetidos.append(num)
print("Lista sin duplicados:", numeros_sin_repetidos)