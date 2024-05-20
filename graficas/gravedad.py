import matplotlib.pylab as plt

def grafica(x,y):
    plt.title('Fuerza en Newtons para diferentes distancias')
    plt.xlabel('Distancia')
    plt.ylabel('Fuerza en N')
    plt.plot(x, y, marker = 'o')
    plt.show()

def data():
    G = 6.674 * (10**(-11))
    m = 0.5 * 1.5
    r = range(100, 1001, 50)
    y = []

    for i in r:
        F = (G * m)/(i**2)
        y.append(F)
    
    grafica(r,y)

if __name__=='__main__':

    data()

