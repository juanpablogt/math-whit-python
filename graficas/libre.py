import matplotlib.pylab as mno

def graf():

    x_eje = [1,2,3,4,5,6,7]
    y_eje = range(1,8)

    mno.plot(x_eje, y_eje, 'o')
    mno.show()

if __name__=='__main__':

    graf()