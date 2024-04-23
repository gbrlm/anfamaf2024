# laboratorio 2 - ejercicio 6
from lab2eje5 import ripf

def phi(x):
    return 2**(x-1)

x0 = 1.6
err = 1e-5
mit = 1000

hx = ripf(phi, x0, err, mit)

print(hx)
print("")
print(hx[-1])