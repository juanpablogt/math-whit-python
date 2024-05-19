from pylab import show,plot,xticks

tem = [5.3,4.5,23.3,12.4,11.5]
years = range(1991,1996)
plot(years, tem, marker='o')

#Fija el eje x como enteros
xticks(years)

show()