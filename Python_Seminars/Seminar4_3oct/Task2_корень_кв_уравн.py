# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python


# Вариант 1 Уравнения

import math

def roots_quadratic_equation(a, b, c):
    discr = b ** 2 - 4 * a * c
    print('Дискриминант D = %.2f' % discr)
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print('2 корня')
        print('x1 = %.2f \nx2 = %.2f' % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        print('1 корень')
        print('x = %.2f' % x)
    else:
        print('Корней нет')

print('Вид уравнения -> ax^2 + bx + c = 0')
print('Введите коэффициенты для уравнения:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
print(f'{a}x^2 + {b}x + c = 0')
roots_quadratic_equation(a, b, c)


# Вариант 2 Встроенная функция

import sympy

print('Введите коэффициенты для уравнения:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

x = sympy.Symbol('x')
f = a * x ** 2 + b * x + c
answer = sympy.solve(f, x)
print(f'{f} => {answer}')

