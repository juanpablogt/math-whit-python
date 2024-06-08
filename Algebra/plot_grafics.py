from sympy import Symbol
from sympy.plotting import plot
#Grafica cualquier funcion

x = Symbol('x')

p = plot(2*x*x*x+5,3*x+2*x+3,2*x, legend = True,show=False)#Muestra leyenda

#Cambiar color
p[0].line_color = 'b'
p[1].line_color = 'r'
p[2].line_color = 'g'

p.show()