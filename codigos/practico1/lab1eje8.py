# laboratorio 1 - ejercicio 8
import math

# Funcion "mala"
def mala(a,b,c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        print("La ecuacion no tiene soluciones reales")
        return None, None  # No hay soluciones reales
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2

# Funcion "buena"
def buena(a,b,c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        print("La ecuacion no tiene soluciones reales")
        return None, None  # No hay soluciones reales
    else:
        if b >= 0:
            x1 = (-b - math.sqrt(discriminante)) / (2*a)
            x2 = (2*c) / (-b - math.sqrt(discriminante))
        else:
            x1 = (2*c) / (-b + math.sqrt(discriminante))
            x2 = (-b + math.sqrt(discriminante)) / (2*a)
        return x1, x2

[x_1,x_2] = buena(1,0,-1)
print([x_1,x_2])