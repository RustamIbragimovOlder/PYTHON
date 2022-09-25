# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

point_one = list(map(int, input('Введите через пробел координаты X и Y точки A -> ').split()))
point_two = list(map(int, input('Введите через пробел координаты X и Y точки B -> ').split()))
distance_AB = round(float(((point_one[0] - point_two[0]) ** 2 + (point_one[1] - point_two[1]) ** 2) ** 0.5), 2)
print('- A', point_one, ';', 'B', point_two, '->', distance_AB)