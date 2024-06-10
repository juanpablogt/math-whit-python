from sympy import FiniteSet
from fractions import Fraction

# se pueden ingresar enteros,draciones y flotantes
a = FiniteSet(1,2,3,4, Fraction(2,3),1.2,2,2)

print(a)

#ignorar el repetidos
print(FiniteSet(*a))