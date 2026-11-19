def anyadir(elem, lista = []) -> list:
    if lista is None:
        lista = []
    lista.append(elem)
    return lista

l = [4, 5, 6]
print(anyadir(1, l))
print(anyadir(1, l))
print(anyadir(1, l))