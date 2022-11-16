from random import randint

x = randint(0, 100) # задание случайного числа от 0 до 100
print(x)

# Компьютер загадал число. Как его найти?

# Вариант 1. Метод последовательного перебора
count_perebor = 0 # счетчик итераций
for i in range(0, 101):
    count_perebor += 1
    if i == x:
        print(f'Метод последовательного перебора. Число найдено! x = {i}')
        print(f'Потребовалось {count_perebor} итераций')
        break

# Вариант 2. Метод случайного угадывания
count_random = 1 # счетчик итераций
y = randint(0, 100)
while x != y:
    y = randint(0, 100)
    count_random += 1
print(f'Метод случайного угадывания. Число найдено! x = {i}')
print(f'Потребовалось {count_random} итераций')

# Вариант 3. Метод бинарного поиска
count_bynary = 1 # счетчик итераций
print('Давай сыграем. Угадай число от 0 до 100!')
y = int(input('Введи число => '))
while x != y:
    if x < y: print('Я загадал меньше')
    else: print('Я загадал больше')
    y = int(input('Введи число => '))
    count_bynary += 1
print(f'Метод бинарного поиска. Число найдено! x = {y}')
print(f'Потребовалось {count_bynary} итераций') 

print(f'Загаданное число => {x}')