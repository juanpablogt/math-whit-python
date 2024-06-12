import random
#Juego para adivinar un numero del 1 al 10
x = random.randint(1,10)
nume = 11
while nume != x:
    if nume == 0:
        print('Fin')
        exit()

    nume = int(input('Adivina el numero: '))

print('°°°HAZ ADIVINADO°°°')