#es una solucion ineficiente
def primo(a):
    prim = []
    for i in range(1,(a+1)):
        nume = 0
        for j in range(1,(a+1)):
            if i % j == 0:
                nume+=1
        if nume == 2:
            prim.append(i)
    print(prim)

primo(100)