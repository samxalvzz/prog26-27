"""
6. Escribir una función eliminar_duplicados(lista) que reciba una lista de elementos
y la modifique eliminando los elementos repetidos, de forma que sólo aparezcan una
vez, en el mismo orden en el que aparecen en la lista.
Ejemplo:
>>> datos = [1, 2, 4, 3, 2, 4, 5, 6, 2]
>>> eliminar_duplicados(datos)
>>> print(datos)
[1, 2, 4, 3, 5, 6]
(Nota: El último 1 no se elimina porque no es consecutivo a los primeros).
"""

def eliminar_duplicados(lista: list) -> None:
    i = 1
    while i < len (lista):
        if lista[i] == lista[i - 1]:
            lista.pop(i)
        else:
            i += 1

def eliminar_duplicados_consecutivos(lista: list) -> None:
    i = 0
    while i < len(lista) - 1:
        if lista[i] == lista[i + 1]
            del lista[i + 1]
        else:
            i += 1
            