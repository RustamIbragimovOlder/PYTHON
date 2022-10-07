# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

def form_polynomial(k):
    polynom = ''
    for i in range(k + 1):
        if i == 0:
            polynom += str(random.randint(1, 100)) + '*x**' + str(k - i)
        elif i == k:
            polynom += ' + ' + str(random.randint(1, 100))
        elif k - i == 1:
            polynom += ' + ' + str(random.randint(1, 100)) + '*x'   
        else:
            polynom += ' + ' + str(random.randint(1, 100)) + '*x**' + str(k - i)
    return polynom
            


# Полином 1
k_1 = int(input('Введите значение натуральной степени k => '))
polynom_1 = form_polynomial(k_1)
print(f'k = {k_1} => {polynom_1}')
with open('filePT4_4.txt', 'w') as data:
    data.write(polynom_1)

# Полином 2
k_2 = int(input('Введите значение натуральной степени k_2 => '))
polynom_2 = form_polynomial(k_2)
print(f'k = {k_2} => {polynom_2}')
with open('filePT4_4_2.txt', 'w') as data:
    data.write(polynom_2)

