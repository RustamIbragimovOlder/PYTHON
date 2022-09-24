# Напишите программу, которая принимает на вход число N
# и выводит числа от -N до N

# Вариант 1 WHILE ПЛОХО
n = int(input('Введите число N -> '))
i = -n
while i <= n:
    print(i)
    i += 1

# Вариант 2 FOR ХОРОШО
n = int(input('Введите число N -> '))
array = []
for i in range(-n, n + 1, 1):
    array.append(i)
print(array)

# Вариант 2 FOR ХУЖЕ
n = int(input('Введите число N -> '))
array = []
for i in range(-n, n + 1, 1):
    print(i, end = " ")