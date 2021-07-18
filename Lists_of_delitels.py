# объявление функции
def get_factors(num):
    k = []
    for i in range(num + 1):
        if i != 0 and num % i == 0:
            k.append(i)
    return k

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))