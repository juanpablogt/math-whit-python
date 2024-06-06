from sympy import symbols,factor,expand,pprint
#Exportar la libreria con las funciones que se necesitan
x,y = symbols('x,y')
#Definir las variables a utilizar
expre = x**3+3*x**2*y+3*x*y**2+y**3
#se define la expresion algebraica
expre = factor(expre)
pprint(expre)
#Se factoriza y se imprime
expre = expand(expre)
pprint(expre)
#se expande y de imprime

