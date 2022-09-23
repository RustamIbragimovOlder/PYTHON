# Список - пронумерованная, изменяемая коллекция объектов

numbers = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
print(numbers)               # [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]

numbers = list(range(1, 11))
print(numbers)               # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers[0] = 10
print(numbers)               # [10, 2, 3, 4, 5]

for i in numbers:
    i *= 2
    print(i)                  # [20, 4, 6, 8, 10]
print(numbers)                # [10, 2, 3, 4, 5]

# Добавление элемента

colors = ['белый', 'красный', 'синий', 'желтый']
for x in colors:
    print(x)
for x in colors:
    print(x*2)
colors.append('зеленый')      # добавить в конец списка
print(colors)

# Удаление элемента

colors.remove('желтый')
print(colors)

# или del colors[3] -> удалить элемент с индексом 3

del colors[3]
print(colors)
