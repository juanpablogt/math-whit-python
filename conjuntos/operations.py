from sympy import FiniteSet

a = FiniteSet(1,2,3,4)
b = FiniteSet(3,5,6,7,8)

print(a.union(b))
print(a.intersect(b))
