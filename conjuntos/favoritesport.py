from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet
import csv
#Programa que representa en diagramas de venn datos que se encuentran en csv
def readcvs(file):
    futball = set()#Genera un conjunto
    other = set()

    with open(file) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[1] == '1':
                futball.add(row[0])
            if row[2] == '1':
                other.add(row[0])
    
    venn2([futball,other])
    plt.show()

if __name__=='__main__':
    readcvs('sportfavorite.csv')