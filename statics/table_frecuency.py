from collections import Counter

def table(n):
    c = Counter(n)
    comun = c.most_common()
    comun.sort()

    print('number\tfrecuency')
    for n in comun:
        print('{0} \t\t {1}'.format(n[0], n[1]))
    
if __name__=='__main__':

    table3 = [4,5,75,3,12,5,3,12,12,12,3,4,5,6,78,90,8,5,32,34,5,7,2,3]
    table(table3)