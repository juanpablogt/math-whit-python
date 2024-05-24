import matplotlib.pyplot as plt 
def create_bar(data,labels):
    num_bars = len(data)
    positions = range (1,num_bars+1)
    plt.barh(positions, data, align='center')
    plt.yticks(positions,labels)
    plt.xlabel('Steps')
    plt.ylabel('Day')
    plt.title('Number of steps')
    plt.grid()
    plt.show()

if __name__=='__main__':

    steps = [100,50,444,5664,423,3445,666]
    days =['Lunes', 'Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
    create_bar(steps,days)