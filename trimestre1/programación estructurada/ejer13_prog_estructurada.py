"""
13. Los datos de los empleados de una empresa se almacenan en una lista de tuplas, donde
cada tupla representa a un empleado de la siguiente forma:
(nombre, apellidos, salario)
En el programa, los cuatro empleados que tiene la empresa se almacenan en la siguiente
lista:
empleados = [('María', 'González', 1800.23),
('Javier', 'Ruiz', 1630.50),
('Jesús', 'Pérez', 2100.42),
('Rosa', 'Muñoz', 2240.78)]
Se pide escribir un programa que modifique la lista de empleados incrementando en un
10 % el salario de cada empleado y muestre por pantalla el salario total de los empleados
de la empresa.
"""

empleados: list[tuple[str, str, float]] = [
    ('María', 'González', 1800.23),
    ('Javier', 'Ruiz', 1630.50),
    ('Jesús', 'Pérez', 2100.42),
    ('Rosa', 'Muñoz', 2240.78)
]

suma = 0.0
i: int = 0

while i < len(empleados):
    # empleados[i] = (empleados[i][0], empleados[i][1], round(empleados[i][2] * 1.10, 2))
    nombre, apellidos, salario = empleados[i]
    salario = round(salario * 1.10, 2)
    empleados[i] = (nombre, apellidos, salario)
    suma += salario
    i += 1

print(suma)