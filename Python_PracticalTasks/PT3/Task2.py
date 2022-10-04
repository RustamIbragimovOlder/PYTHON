# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Вариант 1 Прямой код

list_check = list(map(int,input('Введите несколько чисел через пробел и нажмите <ENTER> -> ').split()))
result = []
index_1 = 0
index_2 = len(list_check) - 1
if len(list_check) % 2 == 0:
    for i in range(int(len(list_check) / 2)):
        product_pairs_numbers = list_check[index_1] * list_check[index_2]
        result.append(product_pairs_numbers)
        index_1 += 1
        index_2 -= 1
    print(f'{list_check} => {result}')
else:
    for i in range(int(len(list_check) / 2)):
        product_pairs_numbers = list_check[index_1] * list_check[index_2]
        result.append(product_pairs_numbers)
        index_1 += 1
        index_2 -= 1
    result.append(list_check[int(len(list_check) / 2)] ** 2)
    print(f'{list_check} => {result}')

# Вариант 2 Функция

def product(list_check):
    result = []
    index_1 = 0
    index_2 = len(list_check) - 1
    for i in range(int(len(list_check) / 2)):
        product_pairs_numbers = list_check[index_1] * list_check[index_2]
        result.append(product_pairs_numbers)
        index_1 += 1
        index_2 -= 1
    return result

list_check = list(map(int,input('Введите несколько чисел через пробел и нажмите <ENTER> -> ').split()))
if len(list_check) % 2 == 0:
    print(f'{list_check} => {product(list_check)}')
else:
    answer = product(list_check)
    answer.append(list_check[int(len(list_check) / 2)] ** 2)
    print(f'{list_check} => {answer}')

# Вариант 3 Преподаватель

import random
def product_pairs_numbers(mass):
    result = []
    if len(mass) % 2 == 0:
        for i in range(len(mass) // 2):
            result.append(mass[i] * mass[len(mass) - 1 - i])
    else:
        for i in range(len(mass) // 2 + 1):
            result.append(mass[i] * mass[len(mass) - 1 - i])
    return result
a = [random.randint(1, 10) for i in range(9)]
print(a)
print(product_pairs_numbers(a))
