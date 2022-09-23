# Типы данных:

# int       # целые числа
# float     # числа с плавающей точкой
# boolean   # логические
# str       # строки
# list      # список
# None      # без типа

from array import array


value = None
print(type(value)) # Вывод типа переменной
a = 123
b = 1.23
print(a)
print(type(a))
print(b)
print(type(b))
value = 12345
print(value)
print(type(value))

s = 'Hello, "World"' # Строка

# s = 'Hello, \n"World"' # Строка с переходом на новую строку

print(s)             # Вывод строки
print(a, b, s) # Интерполяция (вывод нескольких значений)
print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a, b, s)) # Формат
print(f'{a} - {b} - {s}')             # Интерполяция
print('{1} - {2} - {0}'.format(a, b, s)) # Перемена мест

f = True
print(f)
g = False
print(g)

list = [] # Объявление списка (типа массив)
print(list)
array = [1, 2, 3, 5]
print(array)
set = ['1', '2', 'hello']
print(set)
massiv = ['1', '2', 'hello', 1, 23, 455, 3.56, 4.44, True, False]
print(massiv)

