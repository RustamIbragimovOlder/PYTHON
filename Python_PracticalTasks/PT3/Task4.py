# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Вариант 1 Встроенная функция

decimal_number = int(input('Введите десятичное число -> '))
binary_number = bin(decimal_number)
print(f'{decimal_number} -> {binary_number}')

# Вариант 1 Алгоритм

decimal_number = int(input('Введите десятичное число -> '))
binary_number = ''
temp = decimal_number
while temp > 0:
    binary_number = str(temp % 2) + binary_number
    temp = temp // 2
print(f'{decimal_number} -> {binary_number}')

# Вариант 3 Преподаватель

decimal_number = int(input('Введите десятичное число -> '))
print(f'{decimal_number} -> {str(bin(decimal_number)[2 : : ])}')
print(f'{decimal_number} -> {bin(decimal_number)[2 : : ]}')