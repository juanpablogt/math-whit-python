from pylab import plot, show, xticks, legend, title, xlabel, ylabel,axis

list1 = [1.1,2.2,3.4,4.6,5.7,6.8,7.9,8.9]
list2 = [11,21,31,41,51,61,71,81]
list3 = [14,24,53,44,45,64,74,84]
list4 = [15,26,36,46,56,66,76,86]

years = range(1991,1999)

plot(years,list1, years,list2, years,list3, years,list4)

#importa la leyenda
legend(["Eins", "Zwei", "Drei", "Vier"])
title('Temperatura desde 1991 a 1999')
xlabel('years')
ylabel('Temperature')

xticks(years)
show()
