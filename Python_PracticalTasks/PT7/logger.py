# функция записи данных в телефонный справочник
def record_telephone_directory(data):
    with open('telephone_directory.txt', 'a', encoding = 'utf-8') as rec:
        rec.write(f'{data}\n')
    print('Запись произведена')

# функция чтения данных из телефонного справочника
def reading_telephone_directory():
    with open('telephone_directory.txt', 'r', encoding = 'utf-8') as f:
        return f.read()
        