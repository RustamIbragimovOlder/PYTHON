# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Мой старый вариант

# list_check = list(map(int,input('Введите несколько чисел через пробел и нажмите <ENTER> -> ').split()))
# result = 0
# index = 1
# for i in list_check:
#     if index < len(list_check):
#         result += list_check[index]
#         index += 2
# print(f'{list_check} -> ответ: {result}')

# Мой новый вариант

lst = list(map(int, input('Введите числа через пробел => ').split()))
print(lst)
print(f'сумма элементов списка, стоящих на нечётной позиции =\
 {sum([lst[i] for i in range(len(lst)) if i % 2])}')

# возможные варианты задания списков:
# 1. через range
# 2. через random
# 3. через range/random
# 4. чтение из файла и т.д.

