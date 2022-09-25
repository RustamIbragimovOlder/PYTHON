# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number = int(input('Введите число, соответствующее номеру четверти плоскости -> '))
if quarter_number < 1 or quarter_number > 4:
    print('Такой четверти не существует!')
elif quarter_number == 1:
    print(quarter_number, '-> x = [0, +∞]; y = [0, +∞]')
elif quarter_number == 2:
    print(quarter_number, '-> x = [0, -∞]; y = [0, +∞]')
elif quarter_number == 3:
    print(quarter_number, '-> x = [0, -∞]; y = [0, -∞]')
elif quarter_number == 4:
    print(quarter_number, '-> x = [0, +∞]; y = [0, -∞]')