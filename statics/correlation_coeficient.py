def corr(x,y):
    n = len(x)

    prod = []
    for xi,yi in zip(x,y):
        prod.append(xi*yi)
    
    sumpro = sum(prod)
    sumx = sum(x)
    sumy = sum(y)

    cuax = sumx**2
    cuay = sumy**2

    squaresx = []
    for i in x:
        squaresx.append(i**2)

    squaresy = []
    for i in y:
        squaresy.append(i**2)

    sumsqx = sum(squaresx)
    sumqy = sum(squaresy)

    num = (n * sumpro - sumx*sumy)
    den = ((n*sumsqx-cuax)*(n*sumqy-cuay))**0.5

    corre = num/den

    return corre

if __name__=='__main__':

    x = [90,92,95,96,87,87,90,95,98,96]
    y = [85,87,86,97,96,88,89,98,98,87]

    print(corr(x,y))

