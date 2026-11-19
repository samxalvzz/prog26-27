def suma(x: int, y: int) -> int:
    res = x + y
    return res


def validar_dni(n: str) -> None:
    if len(n) != 9:
        print('El DNI no tiene 9 caracteres.')
        return
    if not n[-1].isalpha():
        print('El último carácter del DNI no es una letra.')
        return
    if not n[:-1].isdigit():
        print('La parte numérica del DNI no está formada por dígitos.')
        return
    num = int(n[:-1])
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    if tabla[num % 23] == n[-1]:
        print('Es correcto.')
    else:
        print('Es incorrecto.')


resultado = suma('a', 'b')

lambda x, y:
