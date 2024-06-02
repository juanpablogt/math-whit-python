from matplotlib import pyplot as plt
def corr(x,y):
    #calcula el tamaö de las variables
    n = len(x)
    #calcula el producto de los dos conjuntos x y
    prod = []
    for xi,yi in zip(x,y):
        prod.append(xi*yi)
    #sumatoria de xy
    sumpro = sum(prod)
    #sumatoria de x and y
    sumx = sum(x)
    sumy = sum(y)
    #Cuadrados de las sumatorias
    cuax = sumx**2
    cuay = sumy**2
    #calculo de cada cuadrado
    squaresx = []
    for i in x:
        squaresx.append(i**2)

    squaresy = []
    for i in y:
        squaresy.append(i**2)
    #sumatoria de los cuadrados
    sumsqx = sum(squaresx)
    sumqy = sum(squaresy)
    #numerador y denomindaor de la correlacion
    num = (n * sumpro - sumx*sumy)
    den = ((n*sumsqx-cuax)*(n*sumqy-cuay))**0.5

    corre = num/den

    return corre

if __name__=='__main__':

    x = [90,92,95,96,87,87,90,95,98,96]
    y = [85,87,86,97,96,88,89,98,98,87]

    #solo grafica de puntos
    plt.scatter(x,y,marker='o')
    plt.show()
    print(corr(x,y))

