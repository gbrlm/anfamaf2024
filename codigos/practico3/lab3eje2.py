# laboratorio 3 - ejercicio 2
def inewton(x,y,z):
    if len(x) != len(y):
        print("No coincide la cantidad de puntos")
        return None

    n = len(x)
    matriz_coefs = [[0.0]*m for m in range(n,0,-1)]

    for i in range(n):
        matriz_coefs[i][0] = y[i]

    for j in range(1,n):
        for i in range(0,n-j):
            matriz_coefs[i][j] = (matriz_coefs[i+1][j-1]-matriz_coefs[i][j-1]) / (x[i+j] - x[i])

    c = matriz_coefs[0]
    w = [horn_newton(zj,x,c) for zj in z]
    return w

def horn_newton(zj,x,coefs):
	n = len(coefs)
	valor = coefs[n-1]
	for i in range(n-2,-1,-1):
		valor = coefs[i] + (zj - x[i])*valor
	return valor

"""
# ejemplo
import matplotlib.pyplot as plt
import math

x = [0,math.pi/2,math.pi]
y = [0,1,0]
z = [-math.pi/2 + math.pi*i/100 for i in range(201)]

w = inewton(x,y,z)

f = [math.sin(zz) for zz in z]

plt.plot(x,y,'o')
plt.plot(z,w,'.',label='polinomio interpolante')
plt.plot(z,f,label='sen(x)')
plt.legend()
plt.show()
"""