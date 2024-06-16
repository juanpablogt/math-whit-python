import matplotlib.pyplot as plt
import random

#sierpinski triangle

def transformation_1(p):
    x = p[0]
    y = p[1]
    return 1/2*(x-y), 1/2*(x+y)

def transformation_2(p):
    x = p[0]
    y = p[1]
    return 1/2*(-x-y)+1, 1/2*(x-y)

def transform(p):
    transformations = [transformation_1, transformation_2]
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
        plt.scatter(x, y, s=0.2, color='orange')  # Usar scatter en lugar de plot
        plt.axis('off')  # Ocultar los ejes
        plt.show()