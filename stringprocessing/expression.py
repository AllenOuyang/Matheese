import sympy as sy

def function(sym, expression, val):
    x = sy.Symbol(sym)
    expr = sy.simplify(expression)
    return expr.subs(x, val)

def function2D(sym1, sym2, expression, val1, val2):
    x = sy.Symbol(sym1)
    y = sy.Symbol(sym2)
    expr = sy.simplify(expression)
    tmp = expr.subs(x, val1)
    return tmp.subs(y, val2)

if __name__ == '__main__':
    from sympy import *
    from IPython.display import display, Math

    init_printing()
    x, y, z = symbols("x y z")

    x = y + cos(x) / x
    display(Math('x = ' + latex(x)))