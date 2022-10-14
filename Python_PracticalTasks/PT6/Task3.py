# Напишите программу, которая принимает на вход два числа
# и проверяет, является ли одно число квадратом другого.


# 1. Мой вариант
data = list(map(int, input('Введите два числа через пробел => ').split()))

def square_check(a, b):
    if a * a == b or b * b == a:
        print(True)
    else: print(False)

square_check(data[0], data[1])

# 1. Вариант преподавателя

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
x = lambda a, b: a**2 == b or b**2 == a
print(x(a, b))

