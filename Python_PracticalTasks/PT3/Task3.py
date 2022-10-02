# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_check = list(map(float,input('Введите несколько вещественных чисел через пробел -> ').split()))
print(list_check)
fractional_part_element = []
for i in list_check:
    if (i - int(i)) > 0:
        fractional_part_element.append(round(i - int(i), 5))
print(f' => {max(fractional_part_element) - min(fractional_part_element)}')
