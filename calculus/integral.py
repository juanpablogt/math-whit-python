from sympy import Integral,Symbol,pprint,sympify
#simbolos para utilizar en la integral
x = Symbol('x')
k = Symbol('k')

c = k+x #Integral
i = Integral(c,(x,0,5)).doit #integral definida

pprint(i)