# Напишите программу, которая определит позицию
# второго вхождения строки в списке либо сообщит,
# что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# from itertools import count
# from operator import index

# Var 1
# list_check = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# find_str = "qwe"
# count = 0
# index = -1
# for i in range(len(list_check)):
#     if list_check[i] == find_str:
#         count += 1
#         if count == 2:
#             index = i
#             break
# print(f"список: {list_check}, ищем: '{find_str}', ответ: {index}")

# Var 2
list_check = ["123", "234", 123, "567"]
find_str = "123"
index = [i for i in range(0, len(list_check)) if list_check[i] == find_str]
if len(index) > 1:
    print(f"список: {list_check}, ищем: '{find_str}', ответ: {index[1]}")
else:
    print(f"список: {list_check}, ищем: '{find_str}', ответ: -1")
