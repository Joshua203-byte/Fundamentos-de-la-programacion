'''
Clase:        6
Tema:         Números líderes
Ejercicio:    Imprimir todos los valores líderes de una lista
Descripción:  Imprimir todos los números líderes en una lista. Un número es líder si es mayor que todos los números a su derecha.

Autor:        Joshua Garcilazo
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''
numeros = list(map(int, input().split(' ')))
lideres = []

for i in range(len(numeros) - 1):
    es_lider = True
    for j in range(i + 1, len(numeros)):
        if numeros[i] <= numeros[j]:
            es_lider = False
            break
    if es_lider:
        lideres.append(numeros[i])

print(' '.join(map(str, lideres)))

