def sum_data(filename):
    s = 0
    #abre el archivo e itera sobre el con el nombre de f
    with open(filename) as f:
        for line in f:
            s = s + float(line)
    print('suma de los datos del archivo {0}'.format(s))

if __name__  == '__main__':
    sum_data('mydata.txt')
#El archivo en el mismo directorio no funciono, lo puse en el directorio principal y funciona