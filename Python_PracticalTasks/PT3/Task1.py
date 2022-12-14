# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Вариант 1

list_check = list(map(int,input('Введите несколько чисел через пробел и нажмите <ENTER> -> ').split()))
result = 0
index = 1
for i in list_check:
    if index < len(list_check):
        result += list_check[index]
        index += 2
print(f'{list_check} -> ответ: {result}')

# Вариант 2

list_check = list(map(int,input('Введите несколько чисел через пробел и нажмите <ENTER> -> ').split()))
list_odd_elements = []
for i in range(len(list_check)):
    if i % 2 != 0:
        list_odd_elements.append(list_check[i])
result = sum(list_odd_elements)
print(f'{list_check} -> {list_odd_elements}')
print(f'ответ -> {result}')

# Вариант преподавателя

import random
def sum_odd_elements(mass):
    count = 0
    for i in range(1, len(mass), 2): # проход по массиву с 1-го элемента до конца
        count += mass[i]
    return count

a = [random.randint(1, 10) for i in range(5)]
print(a)
print(sum_odd_elements(a))


