def primo(a):
    nume = 0
    prim = []
    for i in range(1,(a+1)):
        if a % i == 0:
            nume += 1
    
    if nume == 2:
        print("el numero es primo")
    
    else:
        print("el numero no es primo")

primo(35)
