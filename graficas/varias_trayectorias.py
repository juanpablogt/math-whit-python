from matplotlib import pyplot as plt
import math

def grafica(x,y):
    plt.plot(x,y)
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.title('Projectile Motion')

def times(start,end,increment):
    times = []

    while start < end:
        times.append(start)
        start = start + increment
    return times

def positions(u,theta):
    theta = math.radians(theta)
    g = 9.8

    f_time = 2*u*math.sin(theta)/g
    intervals = times(0,f_time,0.001)

    x = []
    y = []

    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
        grafica (x,y)

if __name__=='__main__':
    velocitys = [10, 20, 40]
    a = 45
    for u in velocitys:
        positions(u,a)

    plt.legend(['10','20','40'])
    plt.show()