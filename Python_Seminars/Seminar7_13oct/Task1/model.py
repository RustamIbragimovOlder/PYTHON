import sympy

def evaluate_expr(expr):
    x = sympy.Symbol('x')
    return str(sympy.solve(expr, x))

    