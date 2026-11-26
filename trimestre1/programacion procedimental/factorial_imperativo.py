fact = lambda n: 1 if n == 0 else n * fact(n - 1)

def fact(n: int) -> int:
    if n == 0:
        return 1
    return n * fact(n - 1)

def fact(n: int) -> int:
    """
    Calcula el factorial de un número.
    
    Args:
        n (int): El número al que hay que calcular el factorial.
                 Debe ser mayor o igual que cero.
    
    Returns:
        (int): El factorial de n.
    
    >>> fact(5)
    120
    >>> fact(0)
    1 
    """

    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res

print(fact(5))