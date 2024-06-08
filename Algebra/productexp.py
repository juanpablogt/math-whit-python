from sympy import expand, sympify,pprint
from sympy.core.sympify import SympifyError

def multexp(exp1,exp2):

    product =(exp1*exp2)
    pprint(product)

if __name__ == '__main__':

    ex1 = input('Expresion1: ')
    ex2 = input('Expresion2: ')

    try:
        ex1 = sympify(ex1)
        ex2 = sympify(ex2)
    except SympifyError:
        print('Invalid Imput')
    else:
        multexp(ex1,ex2)