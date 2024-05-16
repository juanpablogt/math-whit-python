def cuadratica(a,b,c):

    D = ((b**2)-(4*a*c))**0.5
    x1 = (-b + D)/(2*a)
    x2 = (-b - D)/(2*a)

    print ("X1: {0}".format (x1))
    print ("X2: {0}".format (x2))
    

cuadratica(-1,7,-10)