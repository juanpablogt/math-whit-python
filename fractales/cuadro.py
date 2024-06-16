import matplotlib.pyplot as plt
import random
import math

#sierpinski triangle

def transformation_1(p):
    x = p[0]
    y = p[1]
    return x/3, y/3

def transformation_2(p):
    x = p[0]
    y = p[1]
    return x/3 + 1/3, y/3

def transformation_3(p):
    x = p[0]
    y = p[1]
    return x/3 + 2/3, 0.5*y + y/3

def transformation_4(p):
    x = p[0]
    y = p[1]
    return x/3 , y/3 + 1/3

def transformation_5(p):
    x = p[0]
    y = p[1]
    return x/3 + 2/3, y/3 + 1/3

def transformation_6(p):
    x = p[0]
    y = p[1]
    return x/3 , y/3 + 2/3

def transformation_7(p):
    x = p[0]
    y = p[1]
    return x/3 + 1/3, y/3 + 2/3

def transformation_8(p):
    x = p[0]
    y = p[1]
    return x/3 + 2/3, y/3 + 2/3

def transform(p):
    transformations = [transformation_1, transformation_2, transformation_3,transformation_4,transformation_5,transformation_6,transformation_7,transformation_8]
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