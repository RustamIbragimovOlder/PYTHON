# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.
# ['ffff', '3rfhg', '4'] -> YES

mass = ['ffff', '3rfhg']
result = 'NO'
for i in mass:
    try:
        int(i)
        result = 'YES'
        break
    except:
        pass
print(f'{mass} -> {result}')
