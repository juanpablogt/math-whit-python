from matplotlib import pyplot as plt
from matplotlib import animation

def create_circle():#Se crea un circulo con radio y centro y se retorna
    circle = plt.Circle((0,0),0.05)
    return circle

def up_radius(i,circle):#Esta es la funcion que aumenta el radio en cada cuadro y cambia el color segun la condicion
    circle.radius = i*0.5
    if i % 2 == 0:
        circle.set_color('orange')
    else:
        circle.set_color('red')
    return circle,

def create_animation():
    fig=plt.gcf()
    ax = plt.axes(xlim=(-10,10), ylim=(-10,10))
    ax.set_aspect('equal')
    circle = create_circle()
    ax.add_patch(circle)
    #Se define el lienzo y se crea el circulo
    anim = animation.FuncAnimation(fig, up_radius, fargs=(circle,), frames=20, interval=100)
    #Esta linea es la que hace la animacion, up_radius cambia en cada cuadro
    plt.title('animation circle')
    plt.show()

if __name__=='__main__':
    create_animation()