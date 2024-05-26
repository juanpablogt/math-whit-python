def mean(n):
    sume = sum(n)
    number = len(n)

    media = sume/number

    return media

if __name__ == '__main__':
    list1 = [1,2,3,4,5,6,7,8,9]

    M = mean(list1)
    N = len(list1)
    print('el numero de datos es {0} y la media es {1}'.format(N,M))
