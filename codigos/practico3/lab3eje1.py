# laboratorio 3 - ejercicio 1
def ilagrange(x, y, z):
    if len(x) != len(y):
        print("No coincide la cantidad de puntos")
        return None
    w = []
    for z_i in z:
        # sumatoria de los polinomios basicos por y_i
        w_i = 0.0
        for idx in range(len(y)):
            # productoria para generar el polinomio base l_i evaluado en z_i
            l_i = 1.
            for jdx in range(len(x)):
                if jdx != idx:
                    l_i = l_i * (z_i - x[jdx]) / (x[idx] - x[jdx])
            w_i = w_i + y[idx] * l_i
        w.append(w_i)
    return w

"""
# ejemplo
import matplotlib.pyplot as plt
import math

x = [0,math.pi/2,math.pi]
y = [0,1,0]
z = [-math.pi/2 + math.pi*i/100 for i in range(201)]

w = ilagrange(x,y,z)

f = [math.sin(zz) for zz in z]

plt.plot(x,y,'o')
plt.plot(z,w,'.',label='polinomio interpolante')
plt.plot(z,f,label='sen(x)')
plt.legend()
plt.show()
"""
