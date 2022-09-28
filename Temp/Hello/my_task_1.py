# # Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
# # которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть;
# # * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".

# def arithmetic(arg1, arg2, op):
#     if op == '+':
#         return arg1 + arg2
#     elif op == '-':
#         return arg1 - arg2
#     elif op == '*':
#         return arg1 * arg2
#     elif op == '/':
#         return arg1 / arg2
#     else:
#         return "Неизвестная операция"
# print(arithmetic(10, 2, '+'))
# print(arithmetic(10, 2, '-'))
# print(arithmetic(10, 2, '*'))
# print(arithmetic(10, 2, '/'))
# print(arithmetic(10, 2, '//'))

# Написать функцию is_year_leap, принимающую 1 аргумент — год,
# и возвращающую True, если год високосный, и False иначе.

# def is_year_leap(arg):
#     if arg % 4 == 0:
#         return True
#     else:
#         return False
# arg = int(input('Введите год -> '))
# print(f'{arg} -> {is_year_leap(arg)}')

# def is_year_leap(year):
#     if year % 400 == 0:
#         return True
#     if year % 4 == 0 and year % 100 != 0:
#         return True
#     return False
# year = int(input('Введите год -> '))
# print(f'{year} -> {is_year_leap(year)}')

# Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа): периметр квадрата,
# площадь квадрата и диагональ квадрата.

# import math
# def square(arg):
#     perimeter_square = arg * 4
#     square_area = arg ** 2
#     diagonal_square_1 = (arg ** 2 * 2) ** 0.5
#     diagonal_square_2 = arg * math.sqrt(2)
#     diagonal_square_3 = math.hypot(arg, arg)
#     return(perimeter_square, square_area, diagonal_square_1, diagonal_square_2, diagonal_square_3)
# arg = int(input('Введите сторону квадрата -> '))
# print(f'{arg} -> {square(arg)}')

# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

# def season(arg):
#     if arg == 12 or (arg > 0 and arg < 3): # if month in (12, 1, 2)
#         return 'зима'
#     elif arg > 2 and arg < 6: # if month in (3, 4, 5)
#         return 'весна'
#     elif arg > 5 and arg < 9: # if month in (6, 7, 8)
#         return 'лето'
#     elif arg > 8 and arg < 12: # if month in (9, 10, 11)
#         return 'осень'
#     else:
#         return 'Такого месяца нет'
# arg = int(input('Введите месяц -> '))
# print(f'{arg} -> {season(arg)}')

# Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых
# (каждый год размер его вклада увеличивается на 10%). Эти деньги прибавляются к сумме вклада,
# и на них в следующем году тоже будут проценты.
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму,
# которая будет на счету пользователя.

# def bank(a, years):
#     for year in range(years):
#         a *= 1.1
#     return a
# a = int(input('Введите размер вклада, руб -> '))
# years = int(input('Введите длительность вклада, лет -> '))
# print(f'{a} руб, на {years} лет -> {bank(a, years)}')

# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.

# def is_prime(arg):
#     if arg == 1:
#         return False  # 1 - не простое число
#     for possible_divisor in range(2, arg):
#         if arg % possible_divisor == 0:
#             return False
#     else:
#         return True
# arg = int(input('Введите число -> '))
# print(f'{arg} -> {is_prime(arg)}')

# Написать функцию date, принимающую 3 аргумента — день, месяц и год.
# Вернуть True, если такая дата есть в нашем календаре, и False иначе.

# def is_year_leap(arg):
#     if arg % 4 == 0:
#         return True
#     else:
#         return False

# def date(day, month, year):
#     day_in_month = {1: 31,
#                     2: 29 if is_year_leap(year) else 28,
#                     3: 31,
#                     4: 30,
#                     5: 31,
#                     6: 30,
#                     7: 31,
#                     8: 31,
#                     9: 30,
#                     10: 31,
#                     11: 30,
#                     12: 31}
#     if 1 <= month <= 12 and 1 <= day <= day_in_month[month]:
#         return True
#     return False

# # def date_cheat(day, month, year):
# #     """Проще, но это непедагогично :)"""
# #     import datetime
# #     try:
# #         datetime.date(year, month, day)
# #     except ValueError:
# #         return False
# #     else:
# #         return True

# day = int(input('Введите день -> '))
# month = int(input('Введите месяц -> '))
# year = int(input('Введите год -> '))
# print(f'{day}, {month}, {year} -> {date(day, month, year)}')

# Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать,
# и ключ шифрования, которая возвращает строку, зашифрованную путем применения функции XOR (^)
# над символами строки с ключом. Написать также функцию XOR_uncipher, которая по зашифрованной строке
# и ключу восстанавливает исходную строку.

import itertools
def XOR_cipher(string, key):
    answer = []
    key = itertools.cycle(key)  # Повторяем ключ, чтобы зашифровать всю строку
    for s, k in zip(string, key):
        answer.append(chr(ord(s) ^ ord(k)))
    return ''.join(answer)

# Функция для расшифровки точно такая же
XOR_uncipher = XOR_cipher
