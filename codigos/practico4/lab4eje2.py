# laboratorio 4 - ejercicio 2

import matplotlib.pyplot as plt
import numpy as np

datos_a = np.linspace(0,1,50) # 50 puntos distribuidos equitativamente en [0,1]
datos_b = np.linspace(0,4*np.pi) # 50 puntos distribuidos equitativamente en [0,4pi]
# evaluar las funciones de los items a y b
f_a = np.arcsin(datos_a)
f_b = np.cos(datos_b)


# calcular los polinomio que mejor ajusta en el sentido de cuadrado mínimo
# de grado 0,1,2,3,4 mediante un bucle

# para el item a
for grado in range(5):

    coeficientes = np.polyfit(datos_a,f_a,grado) # obtener los coeficientes del polinomio de grado "grado" que ajuste los pares "(datos_a,f_a)"
    polinomio_ajuste = np.polyval(coeficientes,datos_a) # evaluar el polinomio

    residuos = np.sum(abs(f_a - polinomio_ajuste)) # calcular el residuo somo la suma de los valores absolutos de la diferencia entre f_a y el valor del polinomio
    print(residuos)

    plt.plot(datos_a,f_a,'o')
    plt.plot(datos_a,polinomio_ajuste)
    plt.show()

# para el item b
for grado in range(5):

    coeficientes = np.polyfit(datos_b,f_b,grado)
    polinomio_ajuste = np.polyval(coeficientes,datos_b)

    residuos = np.sum(abs(f_a - polinomio_ajuste))
    print(residuos)

    plt.plot(datos_b,f_b,'o')
    plt.plot(datos_b,polinomio_ajuste)
    plt.show()