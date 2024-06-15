import matplotlib.pyplot as plt

def circle1():
    circle = plt.Circle((0,0), radius=0.5)
    plt.gca().add_patch(circle)
    plt.axis('scaled')
    plt.show()
#funcion para dibujar un circulo, hay que tener en cuenta que el centro es 0,0 si tenemos en cuenta el plano
#cartesiano por defecto solo se veria una esquina del circulo, por eso se utilizan funciones que ubiquen bien el circulo y se muestre correctamente
if __name__=='__main__':
    circle1()
 

