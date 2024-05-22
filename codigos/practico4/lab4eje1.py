# laboratorio 4 - ejercicio 1

import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt('https://raw.githubusercontent.com/gbrlm/anfamaf2024/main/datos/datos1a.dat')


x = datos[:,0]
y = datos[:,1]
"""
Queremos resolver el sistema

a0 *  m     + a1 *   sum(x)  =  sum(y)
a0 * sum(x) + a1 * sum(x**2) = sum(x*y)
"""
# item a

m=len(x)
# a: sum(x)
a=0
for idx in range(m):
    a = a + x[idx]
# b: sum(x**2)
b = 0
for idx in range(m):
    b =  b + x[idx]**2
# c: sum(y)
c = 0
for idx in range(m):
    c = c + y[idx]
# d: sum(x*y)
d = 0
for idx in range(m):
    d = d + x[idx]*y[idx]

a_0 = (b*c - d*a)/(m*b - a**2)
a_1 = (m*d - a*c)/(m*b - a**2)

plt.plot(x, y, '*')
plt.plot(x, a_1 * x + a_0)
plt.title("item a")
plt.show()


# item b

m = len(x)
a = x.sum() # suma de x_i
b = np.dot(x,x) # suma de x_i al cuadrado, np.dot(x,x) es el producto interno de x con x
c = y.sum() # suma de y_i
d = np.dot(x,y) #suma de x_i*y_i

a_0 = (b*c - d*a)/(m*b - a**2)
a_1 = (m*d - a*c)/(m*b - a**2)

plt.plot(x, y, '*')
plt.plot(x, a_1 * x + a_0)
plt.title("item b")
plt.show()

# item c
x = np.linspace(0, 10, 20)
y = 0.75 * x - 0.5
dispersion = np.random.randn(20) # generar una dispersion con distribucion normal de tamaño 20
puntos_con_ruido = y + dispersion # sumar a los puntos y_i la dispersion_i

ajuste = np.polyfit(x, puntos_con_ruido, 1) # obtener los coeficientes de un ajuste polinomial de grado 1
recta_ajustada = np.polyval(ajuste, x) # polyval evalua el polinomio de coeficientes "ajuste" en los puntos "x"

plt.plot(x, y, '*')
plt.plot(x, puntos_con_ruido, 'o')
plt.plot(x, recta_ajustada)
plt.show()
