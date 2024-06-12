import matplotlib as plt
import random
#Juego que apartir de numeros ramdom calcula un puntaje al cual al que llegar

general_score = 20 # Puntaje al que se debe de llegar

def dado():
    return random.randint(1,6)#Genera el numero aleatorio, simula las caras de un dado

if __name__=='__main__':

    score = 0
    intentos = 0

    while score < general_score:
        tiro = dado()
        score += tiro
        print('cara_num:{0}'.format(tiro))
        intentos +=1
#Este ciclo calcula el cuando y con cuantos intetos se llega al puntaje deseado.
print('Ha finalizado del juego tuviste: {0} puntos en {1} intentos'.format(score,intentos))
#Se imprime el resultado y el numero de lanzamientos.