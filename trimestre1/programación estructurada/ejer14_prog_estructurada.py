"""
14. Convertir una cantidad de tiempo (en segundos, Z) en la correspondiente en horas,
minutos y segundos, con arreglo al siguiente formato:
3817 segundos = 1 horas, 3 minutos y 37 segundos
"""

z = int(input("Introduce la cantidad de segundos: "))

horas = z // 3600
resto = z % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{z} segundos = {horas} horas, {minutos} minutos y {segundos} segundos")