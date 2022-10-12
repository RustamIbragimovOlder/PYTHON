# Напишите программу, которая принимает на вход два числа
# и проверяет, является ли одно число квадратом другого.

data = list(map(int, input('Введите два числа через пробел => ').split()))

def square_check(a, b):
    if a * a == b or b * b == a:
        print(True)
    else: print(False)

square_check(data[0], data[1])

