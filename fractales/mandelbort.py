import numpy as np
import matplotlib.pyplot as plt

# Inicializar los valores para el conjunto de Mandelbrot
x_min, x_max = -2.5, 1.0
y_min, y_max = -1.0, 1.0
max_iter = 1000

# Crear una malla de puntos en el plano complejo
x, y = np.linspace(x_min, x_max, 400), np.linspace(y_min, y_max, 400)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Inicializar la imagen
image = np.zeros(Z.shape, dtype=int)

# Proceso de iteración
for i in range(len(y)):
    for j in range(len(x)):
        c = Z[i, j]
        z = 0
        for n in range(max_iter):
            z = z**2 + c
            if abs(z) > 2:
                image[i, j] = n
                break

# Mostrar el conjunto de Mandelbrot
plt.imshow(image, extent=(x_min, x_max, y_min, y_max))
plt.gray()
plt.show()