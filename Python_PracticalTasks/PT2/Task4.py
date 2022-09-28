# Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.


N = int(input('Введите число N -> '))
set = []
for i in range(-N, N + 1, 1):
    # i += 1
    set.append(i)
print(f'- Для N = {N}: {set}')
elements = list(map(int, input('Введите через пробел индексы элементов -> ').split()))
print(elements)
product_elements = 1
for i in elements:
    product_elements *= set[i]
print(f'Произведение элементов на указанных позициях -> {product_elements}')


