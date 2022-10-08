# Виды
# [exp for item in iterable]                                   на выходе список
# [exp for item in iterable (if conditional)]                  на выходе список с условиями
# [exp <if conditional> for item in iterable (if conditional)  сложно, на практике не использовать!

# Пример 1 просто range
# list = []
# for i in range(1, 21):
#     list.append(i)
# print(list)

# list = [i for i in range(10, 31)]
# print(list)

# Пример 2 четные из range
# list = []
# for i in range(1, 21):
#     if i % 2 == 0:
#         list.append(i)
# print(list)

# list = [i for i in range(10, 31) if i % 2 == 0]
# print(list)

# Пример 3 пары (кортежи) из range

# list = [(i, i) for i in range(10, 31) if i % 2 == 0]
# print(list)

# Пример 4 с функцией из range

list = [(i, i**3) for i in range(10, 31) if i % 2 == 0]
print(list)

