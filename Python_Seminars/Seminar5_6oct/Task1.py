# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.
# Пример:
# Ввод: 1 2 4 5 -> 3

# 1. Мой вариант
with open('fileSem5.txt', 'w') as data:
    data.write(input('Введите последовательность натуральных чисел через пробел => '))
data = open('fileSem5.txt', 'r')
list_check = list(map(int, data.read().split()))
data.close()
for i in range(len(list_check) - 1):
    if list_check[i] != list_check[i + 1] - 1:
        print(f'{list_check} => {list_check[i] + 1}')


