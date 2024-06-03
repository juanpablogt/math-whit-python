import matplotlib.pyplot as plt
import csv

#no grafique porque los datos quedan sobrepuestos
def graphic(x,y):
    plt.xlabel('anio 1960')
    plt.ylabel('annio 1961')
    plt.title('Poblacion de Paises')
    plt.plot(x,y)
    plt.show()
#funcion para extraer los datos del archivo csv
def csvopen(file):
#arreglos donde quedaran los datos a extraer
    x = []
    y = []
    z = []
#abrir el archivo
    with open(file) as f:
        reader = csv.reader(f)
        next(reader)
#seleccion de las columnas a extraer en los arreglos(paises, anio 1 y anio 2)
        for row in reader:
            x.append(float(row[1]))
            y.append(float(row[2]))
            z.append(row[0])

    return x,y,z

if __name__ == '__main__':
    print(csvopen('cleaned_data_Task1.csv'))