from sympy import Limit, Symbol,sin
x = Symbol('x')

l =Limit(1/x,x,0,dir='-')
print(l.doit())


l1=Limit(sin(x)/x,x,0,dir='+')
print(l1.doit())