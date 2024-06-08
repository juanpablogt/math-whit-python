from sympy import sympify,pprint
from sympy.core.sympify import SympifyError
#Se importan las librerias sympy


exp = input('Ingrese la expresion: ')

try:
    exp = sympify(exp)
    pprint(exp)

except SympifyError:
    print('datos incorrectos')

