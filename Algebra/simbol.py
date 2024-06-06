from sympy import symbols,factor,expand
#esto imposta las funciones y asigna simbolos de manera conjunta
x,y = symbols('x,y')

#Se define una expresion
mult = (x+y)*(x-y)
#se expande y se factoriza
print(expand(mult))
print(factor(mult))
