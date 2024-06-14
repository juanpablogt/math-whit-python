from matplotlib_venn import venn2
from sympy import FiniteSet
import matplotlib.pyplot as plt
import csv

def leercsv(file):

    futball = set()
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

if __name__ == '__main__':
    leercsv('sport.csv')
            
