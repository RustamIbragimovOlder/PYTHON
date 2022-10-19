# функция выбора режима работы
def selection_mode():
    print('Режимы работы с данными:')
    print('1. Внесение данных\n\
2. Поиск данных\n\
3. Вывод данных\n\
4. Редактирование данных\n\
0. Выход из программы')
    mode = int(input('Выберите режим работы с данными => '))
    return mode

# функция внесения данных нового сотрудника
def add_new_data():
    a = input('Введите данные сотрудника: ID => ')
    b = input('Фамилия => ')
    c = input('Имя => ')
    d = input('Отчество => ')
    e = input('Номер телефона => ')
    g = input('Должность => ')
    h = input('Заработная плата => ')
    data = f'{a} || {b} || {c} || {d} || {e} || {g} || {h}\n'
    return data

# функция поиска данных сотрудника
def data_search(f):
    a = input('Введите данные для поиска: ')
    data = list(filter(lambda x: a in x, f.split('\n')))
    b = '\n'.join(data)
    return b

# функция редактирования данных
def editing_data(s):
    f = list(filter(lambda x: '||' not in x, s.split('||')))
    print('Выберите индекс элемента для редактирования:\n\
ID               -> 0\n\
фамилия          -> 1\n\
имя              -> 2\n\
отчество         -> 3\n\
номер телефона   -> 4\n\
должность        -> 5\n\
заработная плата -> 6')
    # check = list(map(int, input('=> ').split())) # это на потом, если вводить несколько индексов
    check = int(input('=> '))
    print(f'Текущее значение элемента -> {f[check]}')
    new_value = input('Введите новое значение элемента -> ')
    f[check] = f' {new_value} '
    new_data = '||'.join(f)
    return new_data
