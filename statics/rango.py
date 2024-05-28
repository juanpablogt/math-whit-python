def rango(n):

    menor = min(n)
    maximo = max(n)
    r = maximo - menor

    return menor, maximo, r

if __name__=='__main__':

    table3 = [4,5,75,3,12,5,3,12,12,12,3,4,5,6,78,90,8,5,32,34,5,7,2,3]
    menor, maximo, r = rango(table3)

    print('minimo = {0}, maximo = {1}, rango = {2}'.format(menor,maximo,r))