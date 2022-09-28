# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

value = input('Введите вещественное число -> ')
value_gigits = []
for i in value:
    if i.isdigit():
        value_gigits.append(int(i))
sum = 0
for i in value_gigits:
    sum += i
print(f'- {value} -> {sum}')