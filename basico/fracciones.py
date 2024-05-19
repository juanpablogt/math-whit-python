from fractions  import Fraction

def sum(a,b):
    print('Suma: {0}'.format(a+b))

def sub(a,b):
    print('Resta: {0}'.format(a-b))

def mul(a,b):
    print('Multiplicacion: {0}'.format(a*b))

def div(a,b):
    print('Division: {0}'.format(a/b))

if __name__=='__main__':
    a = Fraction(input('Enter the first number: '))
    b = Fraction(input('Enter the second number: '))

    op = input('Introduce the op: ')

    if op == 'add':
        sum(a,b)
    if op == 'sub':
        sub(a,b)
    if op == 'mul':
        mul(a,b)
    if op == 'div':
        div(a,b)