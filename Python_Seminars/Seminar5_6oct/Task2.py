# Дан список чисел.
# Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# 1. Мой вариант

from random import randint

def list_random_numbers():
    import random
    length = int(input('Введите количество чисел -> '))
    min_limit = int(input('Введите нижнюю границу -> '))
    max_limit = int(input('Введите верхнюю границу -> '))
    return [random.randint(min_limit, max_limit) for i in range(length)]

def output(mass):
    increasing_sequence = [mass[0]]
    for i in range(len(mass)):
        if mass[i] > increasing_sequence[len(increasing_sequence) - 1]:
            increasing_sequence.append(mass[i])
    return increasing_sequence

list_check_1 = list(map(int,input('Введите несколько чисел через пробел и нажмите <ENTER> -> ').split()))
list_check_2 = list_random_numbers()
print(f'{list_check_1} => {output(list_check_1)}')
print(f'{list_check_2} => {output(list_check_2)}')


