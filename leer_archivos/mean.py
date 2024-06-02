def mean(archive):
    datos = []

    with open(archive) as f:
        for line in f:
            datos.append(float(line))

    s = sum(datos)
    n = len(datos)

    m = s/n
    print("La media de los datos del archivo es: {0}".format(m))

if __name__ == '__main__':
    mean('mydata.txt')