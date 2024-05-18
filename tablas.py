def tabla1(a):
    for i in range(1, 11):
        print('{0:.2f} x {1} = {2:.2f}'.format(a, i, a*i))

if __name__=='__main__':
    a= input('Ingrese un numero: ')
    tabla1(float(a))