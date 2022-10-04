# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Вариант мой

# list_check = list(map(float,input('Введите несколько вещественных чисел через пробел -> ').split()))
# print(list_check)
# fractional_part_element = []
# for i in list_check:
#     if (i - int(i)) > 0:
#         fractional_part_element.append(round(i - int(i), 5))
# print(f' => {max(fractional_part_element) - min(fractional_part_element)}')

# Вариант преподавателя

# Функция для отделения дробной части в строке
def fl(n):
    res = str(n)
    fif = res.find('.') # поиск точки в элементе
    res = float('0.' + res[fif + 1 : :])
    # где float - перевод в вещественные
    # '0.' + добавляем к результату
    # res[fif + 1 : :] - срез после точки (дробная часть)
    return res

def diff_of_float(mass):
    result = []
    for i in mass:
        result.append(fl(i)) # задействуем первую функцию
    return(max(result) - min(result))

a = [1.01, 22.34, 45.05]
print(diff_of_float(a))

