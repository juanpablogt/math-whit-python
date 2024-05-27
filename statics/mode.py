from collections import Counter

def mode(n):
    c = Counter(n)
    comun = c.most_common()
    max_comun = comun [0][1]

    mod = []

    for num in comun:
        if num[1] == max_comun:
            mod.append(num[0])
    return mod

if __name__=='__main__':

    list2 = [1,2,3,3,4,4,5,6,6,7,8,9]
    d = mode(list2)
    for n in d:
        print(n)