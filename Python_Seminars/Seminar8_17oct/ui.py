from logger import write_new_data as wnd
from logger import read_data as rd
from logger import alter as alt
from model import add_new_data as addnd
from model import data_search as ds
from model import selection_mode as sm
from model import editing_data as ed

while True:
    mode = sm()
    if mode == 1: # вызов функции добавления данных
        wnd(addnd())
    
    elif mode == 2: # вызов функции поиска данных
        print(ds(rd()))

    elif mode == 3: # вызов функции вывода данных
        print(rd())

    elif mode == 4: # вызов функции редактирования данных
        old_str = ds(rd())
        print(old_str)
        while old_str.count('\n') > 0:
            print('Уточните критерии поиска, чтобы получить запись конкретного сотрудника')
            old_str = ds(old_str)
            print(old_str)
        new_str = ed(old_str)
        alt('seminar8_data.txt', old_str, new_str)

    elif mode == 0: # останов программы
        print('Работа закончена')
        break
    
    else:
        print(f'Режим {mode} находится в разработке')