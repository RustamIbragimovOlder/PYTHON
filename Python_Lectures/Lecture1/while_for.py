# while -> цикл

a = int(input('Введите число -> '))
inverted_a = 0
while a != 0:
    inverted_a = inverted_a * 10 + (a % 10)
    a //= 10
print(inverted_a)


# while-else -> цикл с продолжением после цикла

a = int(input('Введите число -> '))
inverted_a = 0
while a != 0:
    inverted_a = inverted_a * 10 + (a % 10)
    a //= 10
else:
    print('Наверное,')
    print('хватит!')
print(inverted_a)


# for -> Когда мы знаем, что хотим
# for Переменная in Итеррируемый объект

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for abs in list:
    print(abs)
    print(abs**2)


# Использование range

set = range(10)
for i in set:
    print(i) # Печать чисел от 0 до 9

# или

for i in range(7):
    print(i) # Печать чисел от 0 до 6

# или

for h in range(3, 15):
    print(h) # Печать чисел от 3 до 14

# или

for g in range(3, 15, 2):
    print(g) # Печать чисел от 3 до 14 с шагом 2 (нечетные)

# или для строк

for j in 'qwer ty':
    print(j) # Печать всех элементов строки