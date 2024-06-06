from sympy import Symbol,pprint,init_printing

def serie(n):
    
    x = Symbol('x')
    series = x
    init_printing(order='rev-lex')

    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series)

if __name__ == '__main__':
    n = input('Escribe hasta donde ira la serie: ')
    serie(int(n))