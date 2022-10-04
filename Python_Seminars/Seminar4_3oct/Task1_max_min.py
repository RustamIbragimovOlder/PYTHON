# Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# Мой вариант 1 (встроенная функция)

import random
length = int(input('Введите количество чисел -> '))
min_limit = int(input('Введите нижнюю границу -> '))
max_limit = int(input('Введите верхнюю границу -> '))
list_cheсk = [random.randint(min_limit, max_limit) for i in range(length)]
print(f'{" ".join(map(str, list_cheсk))} -> {max(list_cheсk)} {min(list_cheсk)}')

# Мой вариант 2 (алгоритм)

def max_number(mass):
    max = mass[0]
    for i in mass:
        if i > max:
            max = i
    return max

def min_number(mass):
    min = mass[0]
    for i in mass:
        if i < min:
            min = i
    return min

def random_list(length, min_limit, max_limit):
    mass = [random.randint(min_limit, max_limit) for i in range(length)]

import random
length = int(input('Введите количество чисел -> '))
min_limit = int(input('Введите нижнюю границу -> '))
max_limit = int(input('Введите верхнюю границу -> '))
list_cheсk = random_list
print(f'{" ".join(map(str, list_cheсk))} -> {max_number(list_cheсk)} {min_number(list_cheсk)}')

# Вариант коллег



