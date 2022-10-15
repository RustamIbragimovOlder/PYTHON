import module
import logger

print('')
print('Добро пожаловать в телефонный справочник!')
print('')
print('Для выбора режима нажмите:\n добавление данных - <1>\n поиск абонента - <2>\n вывод справочника - <3>')
print('')
a = int(input ('=> '))
if int(a) == 1:
    logger.record_telephone_directory(module.adding_data())
elif a == 2:
    print(module.search_subscriber(logger.reading_telephone_directory()))
elif a == 3:
    print(logger.reading_telephone_directory())
else:
    print('Такой режим находится в разработке')