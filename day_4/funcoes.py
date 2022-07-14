"""Exemplos de funcoes"""

"""
f(x) = 5 * (x / 2)
"""


def f(x):
    result = 5 * (x // 2)
    return result


print(f(10) == 25)

#################################################


def heron(a, b, c):
    """Calcula a area de um triangulo."""
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return area**0.5  # math.sqrt(area)


triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (3, 7, 8),
    (3, 2, 3),
    (3, 4, 5),
]


for triangulo in triangulos:
    area = heron(*triangulo)
    print(f"A area do triangulo e {round(area, 2)}")
