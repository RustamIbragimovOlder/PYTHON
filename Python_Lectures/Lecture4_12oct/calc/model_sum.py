x = 0
y = 0

# метод инициализации (указания значений)
def init(a, b):
    global x #ссылка на певрое упоминание переменной
    global y
    x = a
    y = b

# метод возвращающий результат
def do_it():
    return x + y

