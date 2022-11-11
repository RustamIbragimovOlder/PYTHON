# f(x) = 5x^2 + 10x - 30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0


def diskr(a, b, c):
    return(b**2 - 4*a*c)

def solve(a, b, c):
    d = diskr(a, b, c)
    if d < 0:
        return ['Корней нет']
    elif d == 0:
        return [(-b + d**(0.5))/(2*a)]
    else:
        return [((-b + d**(0.5))/(2*a), (-b - d**0.5)/(2*a))]

def top(a, b, c):
    return (-b/(2*a))

def upnd(a, b, c):
    x = 0
    while True:
        y = 5*x**2 + 10*x - 30
        y1 = 5*x**2 + 10*x - 30



a = int(input())
b = int(input())
c = int(input())
print()





