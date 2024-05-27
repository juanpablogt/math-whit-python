from collections import Counter

def mode(n):
    c = Counter(n)
    comun = c.most_common(1)
    return comun [0][0]

if __name__=='__main__':

    list2 = [1,2,3,4,5,6,6,7,8,9]
    d = mode(list2)
    print('El la moda para el conjunto de numeros es {0}'.format(d))