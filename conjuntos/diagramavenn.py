from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet

def venn(sets):

    venn2(subsets= sets)

    plt.show()

if __name__=='__main__':
    a = FiniteSet(1,2,3,4,5,6,7)
    b = FiniteSet(61,21,343,5,5,6,2,1)
    venn([a,b])
