def menu():
    print('opcion 1: pasar de kilometros a metros')
    print('opcion 2: pasar de metros a kilometros')

def kilo_metro():
    kilo = input('Ingrese el valor en kilometros: ')
    k = float(kilo)

    r = k * 1000
    print('valor en metros: {0}'.format(r))

def metro_kilo():
    metro = input('Ingrese el valor en metros: ')
    m = float(metro)

    r = m / 1000
    print('Valor en kilometros: {0}'.format(r))

if __name__ == '__main__':
    menu()
    a = input('Ingrese una opcion: ')

    if (a == '1'):
        kilo_metro()
    
    if(a == '2'):
        metro_kilo()
    
    else:
        print('\n------------------Valor invalido---------------')
    