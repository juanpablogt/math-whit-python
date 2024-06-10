from sympy import FiniteSet

e = FiniteSet(1,2,3,4,5,6)
a = FiniteSet(1,1,3,1)
b = FiniteSet(2,3,1,1)

v = a.intersect(b)
s = len(v)/len(e)
print(s)