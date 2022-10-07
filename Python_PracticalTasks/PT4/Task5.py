# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# 2*x² + 4*x + 5 3*x² +10*x + 6 Вывод: 5*x² + 14*x + 11

import sympy

x = sympy.Symbol('x')

with open('filePT4_4.txt', "r") as polinom_1:
    a = polinom_1.read()
print(a)

with open('filePT4_4_2.txt', "r") as polinom_2:
    b = polinom_2.read()
print(b)

c = sympy.simplify(a+'+'+b)
with open('filePT4_5.txt', 'w') as f:
    f.write(str(c))
print(c)

