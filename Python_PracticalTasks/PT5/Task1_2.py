# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# Вариант: игра с ботом.

# 1. Мой вариант

game_conditions = 'Условия игры:\n На столе лежит 2021 конфета.\n Играют два игрока делая ход друг после друга.\n Первый ход определяется жеребьёвкой.\n За один ход можно забрать не более чем 28 конфет.\n Все конфеты оппонента достаются сделавшему последний ход.'
print(game_conditions)

from random import randint

# Функция жеребьевки

def draw_function():
    draw = int(input('Для начала жеребьевки нажмите <1> => '))
    if draw == 1:
        A = randint(1, 6)
        B = randint(1, 6)
        print(f'Хозяин => {A} Компьютер => {B}')
        if A > B:
            print('Первый ход делает Хозяин')
            order_moves = ['Хозяин', 'Компьютер']
        elif A < B:
            print('Первый ход делает Компьютер')
            order_moves = ['Компьютер', 'Хозяин']
        elif A == B:
            print('Повторите жеребьевку')
            draw_function()
    return order_moves

# Функция игры

def game_function():
    order_moves = draw_function()
    print('Внимание! Игра начинается!')
    number_candies = 2021
    print(f'На столе {number_candies} конфет')
    stroke_number = 1
    while number_candies > 0:
        print(f'Ход {stroke_number}')
        if order_moves[0] == 'Хозяин':
            motion_A = int(input(f'{order_moves[0]}! Возьмите конфеты => '))
            while motion_A < 1 or motion_A > 29 or motion_A > number_candies:
                print('Столько брать нельзя! Повторите ход. Не меньше 1 и не больше 28.')
                motion_A = int(input(f'{order_moves[0]}! Возьмите конфеты => '))
            number_candies = number_candies - motion_A
            print(f'{order_moves[0]} взял {motion_A} конфет. На столе осталось {number_candies} конфет')
            if number_candies != 0:
                motion_B = randint(1, 29)
                number_candies -= motion_B
                print(f'{order_moves[1]} взял {motion_B} конфет. На столе осталось {number_candies} конфет')
                if number_candies == 0:
                    print(f'Конфеты закончились! Победил {order_moves[1]}!')
                else:
                    stroke_number += 1
            else:
                print(f'Конфеты закончились! Победил {order_moves[0]}!')
        else:
            motion_B = randint(1, 29)
            number_candies -= motion_B
            print(f'{order_moves[0]} взял {motion_B} конфет. На столе осталось {number_candies} конфет')
            if number_candies != 0:
                motion_A = int(input(f'{order_moves[1]}! Возьмите конфеты => '))
                while motion_A < 1 or motion_A > 29 or motion_A > number_candies:
                    print('Столько брать нельзя! Повторите ход. Не меньше 1 и не больше 28.')
                    motion_A = int(input(f'{order_moves[1]}! Возьмите конфеты => '))
                number_candies = number_candies - motion_A
                print(f'{order_moves[1]} взял {motion_A} конфет. На столе осталось {number_candies} конфет')
                if number_candies == 0:
                    print(f'Конфеты закончились! Победил {order_moves[1]}!')
                else:
                    stroke_number += 1
            else:
                print(f'Конфеты закончились! Победил {order_moves[0]}!')

game_function()

number_candies = 2021
print(f'Чтобы выиграть первый игрок должен взять первым ходом {number_candies % 29} конфет')
print(f'А затем выравнивать взятое вторым игроком до 29 (например 1 -> 28, 16 -> 13, 25 -> 4 и т.д.')

# 2. Вариант преподавателя

import random
print("Не останься последним!")
sweets = 117
corch = random.randint(0, 1) # кто будет первый ходить
while sweets > 0:
    if corch == 1: # первый ход - человек
        sweets -= int(input("Сколько заберете?"))
        print("Осталось:", sweets)
        corch = 0 # передача хода компьютеру
    else:
        comp = random.randint(1, sweets % 28)
        sweets -= comp
        print("Компьютер забрал", comp)
        print("Осталось", sweets)
        corch = 1 # передача хода человеку
if corch == 0:
    print("Человек выиграл")
elif corch == 1:
    print("Бот выиграл")
