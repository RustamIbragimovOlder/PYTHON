# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

# Вариант 1

# with open('f.txt', 'a') as data: # запись данных в файл
#     data.write('1 2 3 5 8 15 23 38')

# f = open('f.txt', 'r')
# data = f.read() + ' ' # считывание данных из файла с добавлением пробела
# f.close()
# numbers = []
# while data != '': # проверка: пока строка не пустая
#     space_pos = data.index(' ') # найти первый символ пробела
#     numbers.append(int(data[:space_pos])) # взять все от первого символа до пробела, превратить в число и добавить в новый список
#     data = data[space_pos+1:] # обновляем строку, чтобы не проверять уже проверенное
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e **2))
# print(out)

# Вариант 2 (улучшенный)

# def select(f, col):                             # f - функция, col - набор данных
#     return [f(x) for x in col]                  # формирование списка пока x входит в col
# def where(f, col):                              # f - функция, col - набор данных
#     return [x for x in col if f(x)]             # формирование списка пока x входит в col
# data = '1 2 3 5 8 15 23 38'.split()             # на выходе набор строк

# res1 = select(int, data)                        # вызов функции select для перевода строки в список чисел (int - это функция)
# print(res1)

# res2 = where(lambda e: not e % 2, res1)         # новая функция where для выборки четных чисел 
# print(res2)

# res3 = select(lambda e: (e, e**2), res2)        # функция select принимает res2 и выдает кортежи из пар (исходное число + квадрат)
# print(res3)

# Еще короче вариант без промежуточных переменных
# data = select(int, data)
# data = where(lambda e: not e % 2, data)
# data = list(select(lambda e: (e, e**2), data))
# print(data)

# Вариант с функцией map и filter

data = '1 2 3 5 8 15 23 38'.split()              # ввод данных
data = list(map(int, data))                      # list - перевод в список
                                                 # map - выводит все int каждого элемента data
                                                 # int - перевод в число
print(data)
data = list(filter(lambda e: not e % 2, data))   # list - перевод в список
                                                 # filter - выводит все, которые четные
                                                 # lambda - определяет четность числа
data = list(map(lambda e: (e, e**2), data))      # list - перевод в список
                                                 # map - выводит все кортежи
                                                 # lambda - формирует кортеж (число, квадрат числа)
print(data)