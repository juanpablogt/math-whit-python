from sympy import FiniteSet
import random
#Probabilidad de sumar puntajes con un numero de intentos
def probability(score,intentos):
    caras = FiniteSet(1,2,3,4,5,6)
    s = caras**intentos
    if intentos > 1:
        success_rolls = []
        for elem in s:
            if sum(elem) >= score:
                success_rolls.append(elem)
    
    else:
        if score > 6:
            success_rolls = []
        else:
            success_rolls = []
            for roll in caras:
                if roll >= score:
                    success_rolls.append(roll)
    e = FiniteSet(*success_rolls)
    return len(e)/len(s)

if __name__=='__main__':

    a = int(input('Ingrese el puntaje que quieres obtener: '))
    b = int(input('Ingrese el numero de intentos: '))

    print('La probabilidad de que ocurra es de de: {0}'.format(probability(a,b)))