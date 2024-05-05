def tabla1(a):
    a = input('Ingrese un numero:')
    for i in range(1,11):
        print('{0} x {1} = {2}'.format(a, i,a*i))

tabla1(4)