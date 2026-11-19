fact = lambda n: 1 if n == 0 else n * fact(n - 1)

def fact(n: int) -> int:
    if n == 0:
        return 1
    return n * fact(n - 1)

def fact(n: int) -> int:
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res

