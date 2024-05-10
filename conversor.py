def millas():
    a = 2.54
    inches = input('Ingrese las millas: ')
    b = float(inches)

    ecu = (a*b)/100

    print('valor en metros: ', ecu)

def mill_kilo():
    a = 1.609
    inches = input('Ingrese las millas: ')
    c = float(inches)

    b = a * c
    print('kilometros: ', b)

def temp():
    fahrenheit = input('Ingrese los grados F: ')
    f = float(fahrenheit)
    c = (f-32)*(5/9)

    print('Grados C: ', c)

def temp2():
    celsius = input('Ingrese los C: ')
    c = float(celsius)
    f = (c * 9/5) + 32

    print('Fahrenheit: ', f)

millas()