"""
2. Escribir tres funciones que impriman las siguientes salidas en función de la cantidad de
líneas que se desean ( es un espacio en blanco):
***** * *
***** * ***
***** * *****
***** * *******
"""

def pirame_izquierda(n: int) -> None:
    i = 1
    while i <= n:
        print('*' * 1)
        i += 1

def pirame_derecha(n: int) -> None:
    i = 1
    while i <= n:
        espacios = ' ' * (n - 1)
        asteriscos = '*' * i
        print(espacios + asteriscos)
        i += 1

def piramide_centrada(n: int) -> None:
    i = 1
    while i <= n:
        espacios = ' ' * (n - i)
        asteriscos = '*' * (2 * i - 1)
        print(espacios + asteriscos)
        i += 1