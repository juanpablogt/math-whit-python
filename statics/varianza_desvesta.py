def mean(n):
    s = sum(n)
    nu = len(n)
    me = s / nu
    return me

def dif(n):
    md = mean(n)
    diff = []
    for u in n:
        diff.append(u-md)
    return diff

def cua(n):
    dife = dif(n)
    cu = []
    for i in dife:
        cu.append(i**2)
    n = len(cu)
    val = sum(cu)
    var = val/n
    return var

if __name__=='__main__':
    list2 = [100,60,70,900,100,200,500,500,503,600,1000,1200]
    var = cua(list2)
    print('La varianza es {0}'.format(var))
    #desviacion estandar
    des = var**0.5
    print('La desciacion standar es: {0}'.format(des))