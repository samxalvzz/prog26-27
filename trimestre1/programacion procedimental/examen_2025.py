"""
Debe recibir una lista de tuplas de la forma (valor, cantidad) y
devuelve una nueva lista que contenga _cantidad_ copias del _valor_
original.
"""

from typing import Any

def colapsar(lista: list[tuple[Any, int]]) -> list[Any]:
    """
    Devuelve una lista que contiene elementos repetidos según se
    especifica en las tuplas de la lista original.

    Debe recibir una lista de tuplas de la forma (valor, cantidad) y
    devuelve una nueva lista que contenga _cantidad_ copias del _valor_
    original.
    
    >>> colapsar([(7, 3), (2, 1)])
    [7, 7, 7, 2]
    >>> colapsar([(1, 1), (2, 2), (3, 3)])
    [1, 2, 2, 3, 3, 3]
    >>> colapsar([])
    []
    """
    i = 0
    res = []
    while i < len(lista):
        elem, cant = lista[i]
        res += [elem] * cant
        i += 1
    return res


def compresion_simple(lista: list[int]) -> list[tuple[int, int]]:
    """
    Comprime los elementos repetidos de una lista de enteros.

    Devuelve una lista donde las repeticiones consecutivas son
    sustituidas por tuplas de la forma (valor, cantidad).

    >>> compresion_simple([1, 1, 1, 2, 2, 1, 3])
    [(1, 3), (2, 2), (1, 1), (3, 1)]
    >>> compresion_simple([])
    []
    """
    res = []
    i = 0
    while i < len(lista):
        elem, cant = lista[i], 0
        while i < len(lista) and lista[i] == elem:
            cant += 1
            i += 1
        res.append((elem, cant))
    return res


def normalizar_nombres(nombres: list[str]) -> list[str]:
    """
    Normaliza nombres.

    Recibe una lista de cadenas con posibles espacios extra y que
    mezcla incorrectamente mayúsculas y minúsculas, y devuelve
    una lista con los nombres normalizados.

    - Elimina espacios iniciales y finales.
    - Sustituye varios espacios internos consecutivos por uno solo.
    - Pone la inicial de cada palabra en mayusculas y el resto en
    minúsculas.

    >>> normalizar_nombres(["   Ana   López ", "JOSE   PEREZ  "])
    ["Ana López", "Jose Pérez"]
    """
    def limpiar(nombre: str) -> str:
        return " ".join(nombre.title().strip().split())
    res = []
    i = 0
    while i < len(nombres):
        res.append(limpiar(nombres[i]))
        i += 1
    return res

def test_colapsar1():
    assert colapsar([(7, 3), (2, 1)]) == [7, 7, 7, 2]

def test_colapsar2():
    assert colapsar([(1, 1), (2, 2), (3, 3)]) == [1, 2, 2, 3, 3, 3]

def test_colapsar3():    
    assert colapsar([]) == []
