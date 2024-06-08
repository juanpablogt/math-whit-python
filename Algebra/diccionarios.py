from sympy import symbols


x = symbols('x')
y = symbols('y')

expe = x*y+x+x
#Se utilizan diccionarios para ejecutar la ecuacion con los valores
res = expe.subs({x:1, y:3})

print(res)