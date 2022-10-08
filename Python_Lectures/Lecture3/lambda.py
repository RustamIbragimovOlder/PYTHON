# Анонимные, lambda функции

# # Пример 1
# def sum(x):
#     return x+10
# def mult(x):
#     return x**2
# print(sum(mult(5)))

# # вид lambda
# sum = lambda x: x+10
# mult = lambda x: x**2
# print(sum(mult(2)))
# print(sum(mult(5)))


# # Пример 2
# def sum1(x):
#     return x+22
# def mult2(x):
#     return x**3
# print(sum1(mult2(5)))

# # вид lambda
# sum1 = lambda x: x+22
# mult2 = lambda x: x**3
# print(sum1(mult2(5)))


# # Пример 3
# def sum3(x):
#     return x+242
# def mult4(x):
#     return x**5
# print(sum3(mult4(2)))

# # вид lambda
# sum4 = lambda x: x+242
# mult4 = lambda x: x**5
# sum3(mult4(2))
# print(sum3(mult4(2)))


# # Пример с одной переменной
# def f(x):
#     return x**2
# print(type(f))
# print(f(5))

# def g(x):
#     return x + 30
# print(type(g))
# print(g(5))

# def math(op, x):
#     print(op(x))

# math(f, 15)
# math(g, 10)

# Пример с двумя переменными

# def sum(x, y):
#     return x + y
# sum = lambda q, w: q + w # вид lambda

# def mult(x, y):
#     return x * y
# mult = lambda e, r: e * r # вид lambda

# def calc(op, a, b):
#     return op(a, b)
calc = lambda op, a, b: op(a, b)

# print(calc(sum, 3, 7))
# print(calc(mult, 3, 7))

print(calc(lambda q, w: q + w, 3, 7))
print(calc(lambda e, r: e * r, 3, 7))




