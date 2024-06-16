import matplotlib.pyplot as plt
import random

#sierpinski triangle

def transformation_1(p):
    x = p[0]
    y = p[1]
    return 0.5*x, 0.5*y

def transformation_2(p):
    x = p[0]
    y = p[1]
    return 0.5*x + 0.5, 0.5*y

def transformation_3(p):
    x = p[0]
    y = p[1]
    return 0.5*x + 0.25, 0.5*y + 0.5

def transform(p):
    transformations = [transformation_1, transformation_2, transformation_3]
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