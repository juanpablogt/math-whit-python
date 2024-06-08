from sympy import pprint, init_printing, Symbol #Librerias a utilizar

#Definicion de la funcion para calcular una serie
def ser (n, x_value):
    init_printing(order='rev-lex')
    #orden en el que se imprimira la serie
    x = Symbol('x')

    series = x
    #Calcula la serie y la imprime
    for i in range(2, n+1):
        series = series + (x**i)/i

    pprint(series)
    #Accede a los valores del diccionario que viene en el dato que ingresa el usuario
    series_values = series.subs({x:x_value})
    print ('valor para la serie {0} resultado {1}'.format(x_value,series_values))

if __name__ == '__main__':
    n = int(input('Ingrese numero de terminos de la serie: '))
    x = int(input('Ingrese el valor de x: '))

    ser(n,x)