# Создайте программу для игры в ""Крестики-нолики"".
# Вариант: сам с собой.

playing_field = ['0', '1',  '2', '3', '4', '5', '6', '7', '8']

# Функция вывода игрового поля

def output_playing_field(playing_field):
    for i in range(0, len(playing_field) - 2, 3):
        print(playing_field[i], playing_field[i + 1], playing_field[i + 2])

# Функция проверки победы

def victory_check(playing_field, x, o):
    if playing_field[0] == playing_field[1] == playing_field[2] == 'x' or\
       playing_field[3] == playing_field[4] == playing_field[5] == 'x' or\
       playing_field[6] == playing_field[7] == playing_field[8] == 'x' or\
       playing_field[0] == playing_field[3] == playing_field[6] == 'x' or\
       playing_field[1] == playing_field[4] == playing_field[7] == 'x' or\
       playing_field[2] == playing_field[5] == playing_field[8] == 'x' or\
       playing_field[0] == playing_field[4] == playing_field[8] == 'x' or\
       playing_field[2] == playing_field[4] == playing_field[6] == 'x':
        return True
    elif playing_field[0] == playing_field[1] == playing_field[2] == 'o' or\
       playing_field[3] == playing_field[4] == playing_field[5] == 'o' or\
       playing_field[6] == playing_field[7] == playing_field[8] == 'o' or\
       playing_field[0] == playing_field[3] == playing_field[6] == 'o' or\
       playing_field[1] == playing_field[4] == playing_field[7] == 'o' or\
       playing_field[2] == playing_field[5] == playing_field[8] == '0' or\
       playing_field[0] == playing_field[4] == playing_field[8] == 'o' or\
       playing_field[2] == playing_field[4] == playing_field[6] == 'o':
        return False


# Функция проверки свободных индексов

def checking_free_indexes(playing_field):
    free_indexes = list(filter(lambda a: 'x' not in a and 'o' not in a, playing_field))
    if len(free_indexes) > 0:
        return True
    else:
        return False

# Функция игры

def game_function(playing_field):
    output_playing_field(playing_field)
    for i in range(len(playing_field) - 1):
        if checking_free_indexes(playing_field) == False:
            print('Свободных клеток нет. НИЧЬЯ!')
            break
        else:
            print('Играем дальше!')
        motion_A = int(input(f'Игрок 1! Выберите позицию для x => '))
        while playing_field[motion_A] == 'x' or playing_field[motion_A] == 'o':
            print('Эта позиция занята. Выберите свободную.')
            motion_A = int(input(f'Игрок 1! Выберите позицию для x => '))
        playing_field[motion_A] = 'x'
        output_playing_field(playing_field)
        if victory_check(playing_field, 'x', 'o') == True:
            print('Победа Игрока 1!')
            break
        if checking_free_indexes(playing_field) == False:
            print('Свободных клеток нет. НИЧЬЯ!')
            break
        else:
            print('Играем дальше!')
        motion_B = int(input(f'Игрок 2! Выберите позицию для o => '))
        while playing_field[motion_B] == 'x' or playing_field[motion_B] == 'o':
            print('Эта позиция занята. Выберите свободную.')
            motion_B = int(input(f'Игрок 2! Выберите позицию для o => '))
        playing_field[motion_B] = 'o'
        output_playing_field(playing_field)
        if victory_check(playing_field, 'x', 'o') == False:
            print('Победа Игрока 2!')
            break

print('Допустим: начинает Игрок 1')
game_function(playing_field)




