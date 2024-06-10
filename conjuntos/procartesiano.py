from sympy import FiniteSet
#Imprime todos los conjuntos de a**3
a = FiniteSet(1,2,3,4,5)
b = a**3
print(b)

for i in b:
    print(i)