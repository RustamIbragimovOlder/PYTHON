# Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
# с помощью генераторов списков

# ввод с клавиатуры
# list_check = list(map(int, input('Введите последовательность чисел через пробел => ').split()))
# print(list_check)

# Var 1

# list_check = [1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9]
# result = []
# for i in list_check:
#     if list_check.count(i) == 1:
#         result.append(i)
# print(f'{list_check} -> {result}')

# Var 2

# from random import randint
# min_limit = int(input('Введите нижнюю границу диапазона => '))
# max_limit = int(input('Введите верхнюю границу диапазона => '))
# quantity = int(input('Введите количество элеметов списка => '))
# list_check = [randint(min_limit, max_limit) for i in range(quantity)]
# result = []
# for i in list_check:
#     if list_check.count(i) == 1:
#         result.append(i)
# print(f'{list_check} -> {result}')

# var 3

# list_check = [1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9]
# result = [i for i in list_check if list_check.count(i) == 1]
# print(f'{list_check} -> {result}')

# Var 4

# from random import randint
# min_limit = int(input('Введите нижнюю границу диапазона => '))
# max_limit = int(input('Введите верхнюю границу диапазона => '))
# quantity = int(input('Введите количество элеметов списка => '))
# list_check = [randint(min_limit, max_limit) for i in range(quantity)]
# result = [i for i in list_check if list_check.count(i) == 1]
# print(f'{list_check} -> {result}')


