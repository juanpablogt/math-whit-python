def tabla1(a):
    for i in range(1, 11):
        print('{0:.2f} x {1} = {2:.2f}'.format(a, i, a*i))

if __name__=='__main__':
    while True:
        try:
            a= input('\nIngrese un numero: ')
            print('------------------------')
            tabla1(float(a))
            print('------------------------')
        except ValueError:
            print("\nError ingrese un numero valido\n")
            continue

        volver = input('\nIngrese (y) si quiere salir: ')
        volver = volver.lower()
        if volver == 'y':
            break
        

        