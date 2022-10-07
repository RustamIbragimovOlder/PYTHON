# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def list_random_numbers():
    import random
    length = int(input('Введите количество чисел -> '))
    min_limit = int(input('Введите нижнюю границу -> '))
    max_limit = int(input('Введите верхнюю границу -> '))
    return [random.randint(min_limit, max_limit) for i in range(length)]

def list_non_repeating_elements(a):
    list_check_non = []
    for i in range(len(a)):
        f = True
        for j in range(len(a)):
            if a[i] == a[j] and i != j:
                f = False
                break
        if f == True:
            list_check_non.append(a[i])
    return list_check_non

list_check = list_random_numbers()
print(list_check)
print(list_non_repeating_elements(list_check))
