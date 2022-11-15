import sympy

a, b, c = sympy.symbols('a, b, c')
y1 = a * 31 ** 2 + b * 31 + c - 19310
y2 = a * 51 ** 2 + b * 51 + c - 52150
y3 = a * 61 ** 2 + b * 61 + c - 74570


result = sympy.linsolve([y1, y2, y3], [a, b, c])
print(result)

x = 48
y = 54

f1 = 20 * x ** 2 + 2 * x + 28
f2 = 20 * y ** 2 + 2 * y + 28

print(f1)
print(f2)

