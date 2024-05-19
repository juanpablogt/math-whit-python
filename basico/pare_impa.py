def par_impar(a):
    if a % 2 == 0:
        print("el numero es par")
        print(a)
        for i in range(0,9):
            a +=2
            print(a)
    else:
        print("el numero es impar")
        print(a)
        for i in range(0,9):
            if a % 2 != 0:
                a +=2
            print(a)
par_impar(2)