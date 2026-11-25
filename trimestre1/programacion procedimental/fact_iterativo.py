def fact(n: int) -> int:
    def fact_iter(n: int, acc: int) -> int:
        if n == 0:
            return acc
        return fact_iter(n - 1, acc * n)
    return fact_iter(n, 1)

print(fact(5))