import csv
import matplotlib.pyplot as plt

#dibuja la grafica
def draw(x,y):
    plt.title('Archivo csv')
    plt.xlabel('Numeros')
    plt.ylabel('Squares')
    #dibujar puntos 
    plt.scatter(x,y, marker='o')
    plt.show()

#leer archivo csv
def leer(file):
    #Arreglos para guardar lo que contiene el csv
    x = []
    y = []
    #abrir el archivo e iterar para guardar las posiciones 0 y 1 en los arreglos
    with open(file) as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            x.append(int(row[0]))
            y.append(int(row[1]))
    #llamar la funcion para graficar los puntos
    draw(x,y)

if __name__ == '__main__':
    leer('squares.csv')
