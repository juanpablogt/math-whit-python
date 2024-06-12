import matplotlib as plt
import random


general_score = 20

def dado():
    return random.randint(1,6)

if __name__=='__main__':

    score = 0
    intentos = 0

    while score < general_score:

        tiro = dado()
        score += tiro
        print('cara_num:{0}'.format(tiro))
        intentos +=1

print('Ha finalizado del juego tuviste: {0} puntos en {1} intentos'.format(score,intentos))
