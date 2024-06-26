from sympy import Derivative, Symbol, sympify, pprint
from sympy.core.sympify import SympifyError

def deri(f,var):
    var = Symbol(var) #convierte la variable en un simbolo
    d = Derivative(f,var).doit()#funcion principal que hace la derivacion
    pprint(d) # imprime de forma matematica

if __name__ == '__main__':

    f = input('Ingrese la expresion: ')
    var = input('Ingrese la variable con respecto a la cual se va a derivar: ')
    try:
        f = sympify(f)
    except SympifyError:# si la informacion es invalida imprime el error 
        print('Informacion invalida')
    else:
        deri(f,var)