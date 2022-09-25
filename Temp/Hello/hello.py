msg = "УРА! Hello, World!!!"
print(msg)


point_one = list(map(int, input('Введите через пробел координаты X и Y точки A -> ').split()))
point_two = list(map(int, input('Введите через пробел координаты X и Y точки B -> ').split()))
distance_AB = round(float(((point_one[0] - point_two[0]) ** 2 + (point_one[1] - point_two[1]) ** 2) ** 0.5), 2)
print('- A', point_one, ';', 'B', point_two, '->', distance_AB)
print(f'- A = {point_one}; B = {point_two} -> {distance_AB}')
