# 1. Вызов функции из другого файла

# import functions
# print(functions.f(1))

# 2. Удобство в работе (чтобы не набирать лишнее - меняем на букву)

# import functions as f
# print(f.f(1))

# 3. Значение функции по умолчанию

# def new_string(symbol, count = 3): # 3 - значение по умолчанию и только на последнем месте
#     return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required ...
# print(new_string(4))

# 4. Возможность передачи неограниченного количества аргументов
# 4.1 Строки
# def concatenatio(*params): # * - означает неограниченное количество аргументов

#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# # print(concatenatio(1, 2, 3, 4)) # TypeError: ..

# 4.1 Числа
# def concatenatio(*params): # * - означает неограниченное количество аргументов

#     res: int = 0
#     for item in params:
#         res += item
#     return res
# print(concatenatio(1, 2, 3, 4))

# 5. Рекурсия (функция, которая вызывает сама себя, главное - прописать выход)

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34

# 6. Кортежи (это неизменяемый “список”)
# a, b = 3, 4 # множественное присваивание a = 3, b = 4
# a = (3, 4) # если скобки - кортеж
# b = (3,) # если один элемент - нужна запятая
# print(a)
# print(b)
# print(a[0])

# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')
# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range

# for e in t:
#     print(e) # red green blue

# t[0] = 'black' # TypeError: 'tuple' object does not support
# # item assignment
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t # распаковка кортежа
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue

# 7. Словари (неупорядоченные коллекции произвольных объектов с доступом по ключу)

dictionary = {} # объявление словаря
# \ - служит для того, чтобы писать на новой строке
dictionary = \
    {
        'up': '↑',    # 'up' - ключ, '↑' - значение
        'left': '←',
        'down': '↓',
        'right': '→'
    }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
for k in dictionary.keys: # вывод ключей
    print(k)
for k in dictionary.values: # вывод значений
    print(k)

# типы ключей могут отличаться
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →

# 8. Множества (неупорядоченная совокупность элементов)
# set - тип данных множества
# фигурные скобки - обязательно

# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red') # добавление элемента
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray') # добавление элемента
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red') # удаление элемента
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok # удаление без ошибки
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { } # очистка множества
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8} копирование
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} объединение
# i = a.intersection(b) # i = {8, 2, 5} пересечение?
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}


# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# # {1, 21, 3, 13}

# 8.1. Неизменяемые множества

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})