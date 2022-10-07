# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

from sympy import isprime

def prime_number(a):
    list_check = []
    i = 2
    while i <= a:
        if isprime(i):
            while a % i == 0 and a % i == 0:
                list_check.append(i)
                a = int(a / i)
        i += 1
    return list_check

N = int(input('Введите натуральное число -> '))           # Число вводит пользователь, можно random
if N <= 1:
    print('Некорректный ввод')                            # Натуральное число != 1
else:
    print(f'{N} = {"*".join(map(str, prime_number(N)))}')

