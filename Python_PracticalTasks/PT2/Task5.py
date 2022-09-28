# Реализуйте алгоритм перемешивания списка.

from random import randint
min_limit = int(input('Введите нижнюю границу -> '))
max_limit = int(input('Введите верхнюю границу -> '))
count_value = int(input('Введите количество элементов -> '))
random_numbers = []
for i in range(count_value):
    random_numbers.append(randint(min_limit, max_limit))
print(random_numbers)
import random 
random.shuffle(random_numbers)
print(random_numbers)