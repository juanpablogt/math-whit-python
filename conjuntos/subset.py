from sympy import FiniteSet
# Se definen dos conjuntos
a = FiniteSet(1)
b = FiniteSet(1,2)
#Se pregunta si si uno es subconjunto del otro
print(a.is_subset(b))
print(b.is_subset(a))

#Defino otro conjunto
c = FiniteSet(1,2,3)

#Genera conjunto de sunconjuntos
ps=c.powerset()
print(ps)
#Cuenta cuantos subconjuntos se generaron
print(len(ps))