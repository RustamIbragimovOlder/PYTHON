from random import randint

# Вариант 1. Итерационный метод бинарного поиска

left = int(input('Введите левую границу диапазона => '))
right = int(input('Введите правую границу диапазона => '))
x = randint(left, right) # задание случайного числа от left до right

count_bynary = 1 # счетчик итераций
print('Давай сыграем. Угадай число от 0 до 100!')

mid = (left + right) // 2 # целочисленное деление, находим середину

# запускаем поиск:
while x != mid:
    print(mid)
    if x < mid:
        print('Загаданное число меньше')
        right = mid - 1
    else:
        print('Загаданное число больше')
        left = mid + 1
    mid = (left + right) // 2
    count_bynary += 1
print(f'Метод бинарного поиска. Число найдено! x = {mid}')
print(f'Потребовалось {count_bynary} итераций') 

print(f'Загаданное число => {x}')


# Вариант 1. Рекурсивный метод бинарного поиска

def binary_search_recursive(array, element, start, end):
    if start > end: # условие выхода из рекурсии, если элемента не существует в массиве
        return -1
    mid = (start + end) // 2
    if element == array[mid]:
        return mid
    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid - 1)
    else:
        return binary_search_recursive(array, element, mid + 1, end)
