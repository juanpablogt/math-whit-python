from matplotlib import pyplot as plt
from matplotlib import animation
import math

g = 9.8

def intervals1(u, tetha):
    t_flight = 2*u*math.sin(tetha)/g
    intervals = []
    start = 0
    interval = 0.05  # Corrección aquí: 'interval' es el paso que se añade a la lista 'intervals'
    while start < t_flight:
        intervals.append(start)
        start = start + interval
    return intervals

def position(i, circle, intervals, u, tetha):
    t = intervals[i]
    x = u*math.cos(tetha)*t
    y = u*math.sin(tetha)*t - 0.5*g*t**2  # Corrección aquí: la fórmula para 'y' incluye "t**2"
    circle.center = x, y
    return circle,

def create_animation(u, tetha):
    intervals = intervals1(u, tetha)
    xmin = 0
    xmax = u*math.cos(tetha)*intervals[-1]
    ymin = 0
    t_max = u*math.sin(tetha)/g
    y_max = u*math.sin(tetha)*t_max - 0.5*g*t_max**2  # Corrección aquí: la fórmula para 'y_max' incluye "t_max**2"
    
    # Ajustes en los límites de 'xmax' y 'y_max' pueden ser necesarios dependiendo del ángulo de lanzamiento
    
    fig = plt.gcf()
    ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, y_max))
    circle = plt.Circle((xmin, ymin), 0.1)
    ax.add_patch(circle)
    
    anim = animation.FuncAnimation(fig, position,
                                   fargs=(circle, intervals, u, tetha), frames=len(intervals), interval=1,
                                   repeat=False)  # Corrección aquí: 'interval' en lugar de 'intereval'
    
    plt.title('Movimiento proyectil')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.show()

if __name__ == '__main__':
    try:
        u = float(input('Ingrese la velocidad inicial (m/s): '))
        t = float(input('Ingrese el ángulo en grados: '))
        t = math.radians(t)  # Conversión de grados a radianes
        create_animation(u, t)
    except ValueError:
        print('Valores inválidos')
