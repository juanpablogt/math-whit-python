from sympy import init_printing,symbols, pprint #Define las librerias a utilizar
#Define las variables
x,y = symbols('x,y')
#Define e imprime la expresion en original
expre = 3*x**2*y+3*x*y**2+y**2+1
pprint(expre)
#Define el orden de la expresion
init_printing(order='rev-lex')
pprint(expre)

