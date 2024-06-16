import random
import matplotlib.pyplot as plt
def transformation_1(p):
    x = p[0]
    y = p[1]
    return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6

def transformation_2(p):
    x = p[0]
    y = p[1]
    return 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6

def transformation_3(p):
    x = p[0]
    y = p[1]
    return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44

def transformation_4(p):
    x = p[0]
    y = p[1]
    return 0, 0.16*y 

def transform(p):
    transformations = [transformation_1, transformation_2, transformation_3, transformation_4]
    t = random.choice(transformations)
    x, y = t(p)
    return x, y

def build_trajectory(p, n):
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])
    return x, y

if __name__ == '__main__':
    
    p = (0, 0)
    n = int(input('Introduce el número de iteraciones: '))
    x, y = build_trajectory(p, n)
    plt.scatter(x, y, s=0.2, color='green')  # Usar scatter en lugar de plot
    plt.axis('off')  # Ocultar los ejes
    plt.show()
