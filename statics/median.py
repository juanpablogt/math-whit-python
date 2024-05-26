def median(n):
    N = len(n)
    n.sort()
    if N % 2 == 0:
        m1 = N/2
        m2 = (N/2)+1

        m1 = int(m1)-1
        m2 = int(m2)-1

        median = (n[m1]+n[m2])/2

    else:
        m = (N+1)/2
        m = int(m)-1
        median = n[m]

    return median

if __name__=='__main__':
    list2 = [1,2,3,4,5,6,7,8,9,10]
    print(median(list2))