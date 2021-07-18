from math import *
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep='\n')
elif d == 0:
    x1 = ((-1) * b) / (2 * a)
    x2 = x1
    print(x2)
elif d < 0:
    print('Нет корней')