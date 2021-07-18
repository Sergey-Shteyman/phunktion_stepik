# объявление функции
from math import *


def solve(a, b, c):
    k = []
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (b * (-1) - sqrt(d)) / (2 * a)
        k.append(x1)
        x2 = (b * (-1) + sqrt(d)) / (2 * a)
        k.append(x2)
        k.sort()
        return k
    elif d == 0:
        x1 = ((-1) * b) / (2 * a)
        return x1, x1


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)