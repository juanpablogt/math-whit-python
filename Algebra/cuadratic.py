from sympy import solve,pprint,Symbol
from sympy.core.sympify import SympifyError

#funcion para resolver formula cuadratica utilizando solve
def cuadratic(a,b,c):
    x = Symbol('x')
    exp = a*x*x + b*x + c
    pprint(solve(exp,x,dict=True))#Imprime la ecuacion en funcion de x

if __name__=='__main__':
    a = int(input('Ingrese a:'))
    b = int(input('Ingrese b:'))
    c = int(input('Ingrese c:'))

    try:
        cuadratic(a,b,c)

    except SympifyError:
        print('Datos equivocados')