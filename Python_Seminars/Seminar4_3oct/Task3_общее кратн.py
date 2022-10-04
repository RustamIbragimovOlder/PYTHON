# Задайте два числа.
# Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# Var 1

# a = int(input('Введите число a -> '))
# b = int(input('Введите число b -> '))
a, b = map(int, input('Введите числа a и b через пробел -> ').split())
if a != 0 and b != 0:
    i = min(a, b)
    while True:
        if i % a == 0 and i % b == 0:
            break
        else:
            i += 1
    print(f'{a}, {b} -> {i}')
else:
    print('Делить на 0 нельзя. Проверьте ввод.')

# Var 2 ???

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
# a, b = map(int, input().split())
# print(a * b // gcd(a, b))