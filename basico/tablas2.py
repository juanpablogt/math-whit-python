def tabla(a,b):
    for i in range(1,(b+1)):
        print('{0} x {1} = {2:.1f}'.format(a, i, a*i))

if __name__=='__main__':
    while True:
        try:
            a = input('Ingrese la tabla: ')
            b = input('Ingrese el valor hasta donde va: ')
            print('-------------------------------------')
            x = int(a)
            y = int(b)

            tabla(x,y)
            print('-------------------------------------')
        except ValueError:
            print("\n-----Error, digite numeros enteros-----\n")
            continue

        answer = input('Ingrese (y) si quieres salir: ')
        answer = answer.lower()
        if answer == 'y':
            break