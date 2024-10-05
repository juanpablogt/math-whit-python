from sympy import Integral, Symbol, pprint
# Define symbols for use in the integral
x = Symbol('x')
k = Symbol('k')
# Define the expression for the integral
c = k + x
# Create the definite integral
integral_expr = Integral(c, (x, 0, 5)).doit()
# Pretty print the symbolic form of the integral
pprint(integral_expr)
