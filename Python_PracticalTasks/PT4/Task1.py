# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# Число ПИ (round с округлением)

import math
print(math.pi)
d = int(input('Введите количество знаков после запятой от 1 до 10 -> '))
if d < 1 or d > 10:
    print('Некорректный ввод')
else:
    print(f'd = {10 ** -d}, pi = {round(math.pi, d)}')

# Число ПИ (срез без округления)

import math
print(math.pi)
d = int(input('Введите количество знаков после запятой от 1 до 10 -> '))
if d < 1 or d > 10:
    print('Некорректный ввод')
else:
    result = '3.' + str(math.pi)[2 : d + 2]
    print(f'd = {10 ** -d}, pi = {result}')


