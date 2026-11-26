"""
8. Escribir una función analizar_diagonales(matriz) que reciba una lista de listas de
números, de forma que:
- Si la matriz está vacía o no es cuadrada (es decir, alguna fila no tiene la misma
longitud que el número total de filas),
debe devolver None.
- Si es cuadrada, debe devolver una tupla (suma principal, suma secundaria)
con la suma de su diagonal principal y
su diagonal secundaria
"""

def es_cuadrada(matriz: list[list[int]]) -> bool:
    """
    Suma las diagonales de una matriz, si es cuadrada.

    Args:
        matriz (list[list[int]]): La matriz, almacenada por filas y
            representada como una lista de filas, donde cada fila es una
            lista de enteros.

    Returns:
        None: si la matriz es vacía o no es cuadrada.
        tuple[int, int]: la suma de la diagonal principal y la secundaria,
            en ese orden.

    >>> analizar_diagonales([])
    >>> analizar_diagonales([[1,2], [3, 4], [5, 6]])
    >>> analizar_diagonales([[1, 2, 3], [4, 5, 6], [9, 8, 7]])
    (13, 17) 
    """
    num_filas = len(matriz)
    i = 0
    while i < num_filas:
        num_columnas = len(matriz[i])
        if num_columnas != num_filas:
            return False
        i += 1
    return True

def analizar_diagonales(matriz: list[list[int]]) -> None | tuple[int, int]:
    if matriz == [] or not es_cuadrada(matriz):
        return None
    suma_principal, suma_secundaria = 0, 0
    i = 0
    while i < len(matriz):  # <-- Cambiar '>' por '<'
        suma_principal += matriz[i][i]
        suma_secundaria += matriz[i][-1 - i]
        i += 1
    return (suma_principal, suma_secundaria)

def test_analizar_diagonales():
    assert analizar_diagonales([]) is None, "Matríz vacía"
    assert analizar_diagonales([[1,2], [3, 4], [5, 6]]) is None, "Matríz cuadrada"
    assert analizar_diagonales([[1, 2, 3], [4, 5, 6], [9, 8, 7]]) == (13, 17)

