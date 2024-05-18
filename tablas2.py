def tabla(a,b):
    for i in range(1,(b+1)):
        print('{0} x {1} = {2:.1f}'.format(a, i, a*i))

if __name__=='__main__':
    while True:
        a = input('Ingrese la tabla: ')
        b = input('Ingrese el valor hasta donde va: ')
        x = int(a)
        y = int(b)

        tabla(x,y)

        answer = input('Ingrese (y) si quieres salir: ')
        answer = answer.lower()
        if answer == 'y':
            break