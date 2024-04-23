from lab2eje7 import lab2ej7bisec, lab2ej7newton, lab2ej7ipf
import matplotlib.pyplot as plt
import math
# import numpy as np
# x = np.linspace(0.0, 1.5, 100)

"""
h = 1.5/99
x = [i*h for i in range(100)]
y = [lab2ej7bisec(xi) for xi in x]


plt.plot(x,y)
plt.show()


"""
h = 1.5/99
x = [i*h for i in range(100)]
y_bisec = [lab2ej7bisec(xi) for xi in x]
y_newton = [lab2ej7newton(xi) for xi in x]
y_ipf = [lab2ej7ipf(xi) for xi in x]

"""
plt.plot(x,y_bisec,'o', label="bisec")
plt.plot(x,y_newton,',' label="newton")
plt.plot(x,y_ipf, label="punto fijo")
plt.legend()
plt.show()
"""

fig,ax = plt.subplots(1,3)

ax[0].plot(x,y_bisec,label="bisec",color='green')
ax[0].set_title("Método Bisección")
ax[0].legend()
ax[1].plot(x,y_newton,label="newton",color='blue')
ax[1].set_title("Método Newton")
ax[1].legend()
ax[2].plot(x,y_ipf,label="p. fijo",color='black')
ax[2].set_title("Método Punto Fijo")
ax[2].legend()

plt.show()
