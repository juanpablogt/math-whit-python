from sympy import solve,Symbol#Importando solve

x = Symbol('x')
expr = x**2+3*x+2

print(solve(expr, dict=True))#Imrimiendo en forma de diccionario
