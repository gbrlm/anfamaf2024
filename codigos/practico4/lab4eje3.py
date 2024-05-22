# laboratorio 4 - ejercicio 3

import matplotlib.pyplot as plt
import numpy as np


# item b
datos_b = np.loadtxt('datos3b.dat') # leemos los datos desde el archivo, en la misma carpeta que este archivo

x = datos_b[0,:] # primer fila de los datos corresponden a los valores para x
y = datos_b[1,:] # segunda fila corresponde a los valores de y

# linealizamos la función para hacer el ajuste
xx = x
yy = x/y

m = len(xx)
a = xx.sum()
b = np.dot(xx,xx)
c = yy.sum()
d = np.dot(xx,yy)

a_0 = (b*c - d*a)/(m*b - a**2)
a_1 = (m*d - a*c)/(m*b - a**2)

plt.plot(x, y, '*')
plt.plot(x, x/(a_1*x + a_0))
plt.show()


"""
# item a 

datos_a = np.loadtxt('datos3a.dat')

x = datos_a[0,:]
y = datos_a[1,:]

xx = np.log(x)
yy = np.log(y)

m = len(xx)
a = xx.sum()
b = np.dot(xx,xx)
c = yy.sum()
d = np.dot(xx,yy)

a_0 = (b*c - d*a)/(m*b - a**2)
a_1 = (m*d - a*c)/(m*b - a**2)

plt.plot(x, y, '*')
plt.plot(x, np.exp(a_0)*(x** a_1))
plt.show()
"""