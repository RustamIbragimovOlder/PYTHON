# Напишите программу, которая на вход принимает
# 5 чисел и находит максимальное из них

# Вариант 1
a1 = int(input('Введите 5 чисел -> '))
max = a1
for i in range(4):
    b = int(input())
    if b > max:
        max = b
print('max =', max)

# Вариант 2
a = list(map(int,input().split()))
b = max(a)
print('max =', b)

# Вариант 3
print('max =', max(list(map(int,input().split()))))