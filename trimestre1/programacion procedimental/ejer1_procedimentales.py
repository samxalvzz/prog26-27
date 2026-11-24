"""
1. Considérese la siguiente fórmula (debida a Herón de Alejandría), que expresa el valor
de la superficie S de un triángulo cualquiera en función de sus lados, a, b y c:
𝑆 =
√︄
𝑎 + 𝑏 + 𝑐
2

𝑎 + 𝑏 + 𝑐
2
− 𝑎
 𝑎 + 𝑏 + 𝑐
2
− 𝑏
 𝑎 + 𝑏 + 𝑐
2
− 𝑐

Escribir una función que obtenga el valor 𝑆 a partir de 𝑎, 𝑏 y 𝑐, evitando el cálculo
repetido del semiperímetro, 𝑠𝑝 =
𝑎+𝑏+𝑐
2
, y almacenando el resultado finalmente en la
variable S.
"""

import math

def area_triangulo(a: float, b: float, c: float) -> None:
    sp = (a + b + c) / 2
    S = math.sqrt(sp * (sp - a) * (sp - b) * (sp - c))
    return S