# f(x) = 5x^2 + 10x - 30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

import sympy

x = sympy.Symbol('x')
f = 5*x**2 + 10*x - 30

# Определить корни
k = sympy.solve(f, x)
print(k)

diff = sympy.diff(f, x)

# Найти интервалы, на которых функция возрастает
print(sympy.solve(diff > 0, x))

# Найти интервалы, на которых функция убывает
print(sympy.solve(diff < 0, x))

# Построение графика
sympy.plotting.plot(f)

# Вычислить вершину
print(sympy.solve(diff, x))

# Определить промежутки, на котором f > 0
print(sympy.solve(f > 0, x))

# Определить промежутки, на котором f < 0
print(sympy.solve(f < 0, x))