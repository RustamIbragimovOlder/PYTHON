## арифметические операции
# a = 11 * 2 ** 2 - 13 / 4 + 7
# print(a)

# #Расчет объема памяти
# # 1. Импортируем функцию из модуля
# from sys import getsizeof
# # 2. Находим объем занимаемом памяти в Мегабайтах
# print(getsizeof(3 ** 9090001) / (1024 * 1024))
# # Результат: 1.8319969177246094

# # Максимальное число из трех 4
# print(4 ** 4 ** 4)

# # Функция pos_add(a, b), которая возвращает положительное значение сложения двух целых чисел
# # abc - модуль
# def pos_add(a, b):
#    return abs(a + b)
# print(pos_add(2, 5))
# print(pos_add(-2, 5))
# print(pos_add(-2, -5))

# # Функция foo(a), которая возвращает результат целочисленного и по модулю деления любого целого числа на -11.
# def foo(a):
#    return divmod(a, -11)
# # или
# def foo(a):
#    return a // -11, a % -11
# print(foo(22))
# print(foo(-77))
# print(foo(1))

# # Напишите функцию num_sum(a), принимающую любое значение. 
# # Если это целое число, то возвратить сумму его чисел. 
# # В противном случае возвращается фраза «Это не целое число».

# def num_sum(a):
#    # 1. Определяем принадлежность значения 'a' к целому числу, но не к булеву типу
#    if isinstance(a, int) and not isinstance(a, bool):
#        # 2. Преобразуем число в положительное, а потом - строку
#        a_to_str = str(abs(a))
#        # 3. Задаем начальную сумму 0
#        s = 0
#        # 4. В цикле складываем все числа
#        for i in a_to_str:
#            s += int(i)
#        return s
#    return 'Это не целое число'

# # Тесты
# print(num_sum(-146))
# print(num_sum('-11'))
# print(num_sum(True))

# Дана последовательность случайных цифр любой длины и «волшебное» положительное число, больше нуля. 
# Напишите функцию magic(), принимающую эти аргументы, и выясните, можно ли разделить сумму квадратов последовательности на «волшебное» число без остатка. 
# В качестве ответа возвращается «Волшебство случается» в случае успеха или «Никакого волшебства», если разделить нельзя.

def magic(*args, k):
   # 1. Начальная сумма равна нулю
   sq_sum = 0
   # 2. Складываем квадраты всех аргументов в цикле
   for i in args:
       sq_sum += i ** 2
   # 3. Определяем, равен ли остаток от деления sq_sum на k нулю
   if sq_sum % k == 0:
       return 'Волшебство случается'
   return 'Никакого волшебства'

# Тесты
print(magic(2, 5, 7, k=5))
print(magic(2, 5, 7, k=39))
print(magic(2, 5, 7, k=2))