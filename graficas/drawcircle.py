import matplotlib.pyplot as plt
#Se define el circulo con centro y radio
def circle():
    circle = plt.Circle((0,0), radius=0.5)
    return circle
#Funcion para graficar la figura teniendo en cuenta los ejes y la ubivacion del circulo
def draw(figure):
    ax = plt.gca()
    ax.add_patch(figure)
    plt.axis('scaled')
    plt.show()

if __name__ == '__main__':
    c = circle()
    draw(c)