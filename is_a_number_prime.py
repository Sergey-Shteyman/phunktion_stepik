def number_of_factors(num):
    counter = 0
    for i in range(num + 1):
        if i != 0 and num % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False


# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))