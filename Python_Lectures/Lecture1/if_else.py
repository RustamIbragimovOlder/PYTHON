# if, if-else

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

# Если несколько условий -> elif

name = input('Введите свое имя -> ')
if name == 'Рустам':
    print('Ты молодец, Рустам!')
elif name == 'Андрей':
    print('Ты идиот, Андрей')
elif name == 'Оля':
    print('Оля! Ты супер!')
else:
    print('Привет,', name)
