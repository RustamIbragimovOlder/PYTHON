# # Вариант 1 Запись (если режим 'w' - перезапись)
# colors = ['red1', 'green2', 'blue3'] # набор данных (список)
# data = open('file.txt', 'a') # data - текстовая переменная + связь с текстовым файлом, file.txt - путь к файлу, а - режим работы
# # data.writelines(colors) # функционал для записи данных
# data.write('LINE 2\n')
# data.write('LINE 3\n')
# data.close() # закрытие файла после работы

# # Вариант 2 Запись (закрытие файла после работы не требуется)
# with open('file.txt', 'a') as data:
#     data.write('LINE 1\n')
#     data.write('LINE 2\n')

# Вариант 3 Чтение данных из файла
path = 'file.txt' # путь к файлу
data = open(path, 'r') # открытие в режиме чтения
for line in data: # при помощи цикла считываем все строки
    print(line)
data.close()





