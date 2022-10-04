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

import random
length = int(input('Введите количество чисел -> '))
min_limit = int(input('Введите нижнюю границу -> '))
max_limit = int(input('Введите верхнюю границу -> '))
list_check = [random.randint(min_limit, max_limit) for i in range(length)]
print(f'{" ".join(map(str, list_check))} -> {max_number(list_check)} {min_number(list_check)}')

# Вариант коллег (фиговый!!! Условиям не соответствует)

def input_nums(log = 'Введите строку чисел через пробел -> '):
    try:
        return list(map(int, input(log).split()))
    except:
        return input_nums('Введены не целые числа или не числа. Проверьте ввод!')

def get_min_max(lst):
    return(min(lst), max(lst))

nums = input_nums()
print(get_min_max(nums))

