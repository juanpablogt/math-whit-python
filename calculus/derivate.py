from sympy import Derivative, Symbol

t = Symbol('t')
x = 5*t+3*t*t+2

print(Derivative(x).doit())