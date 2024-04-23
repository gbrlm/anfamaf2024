# laboratorio2 - ejercicio 2
import lab2eje1
import math

def fun_lab2ej2a(x):
    return 2*x-math.tan(x)

def fun_lab2ej2b(x):
    return x**2 - 3
######################################################
I = [0.8,1.4]
err = 10**-5
mit = 100

hx, hy = lab2eje1.rbisec(fun_lab2ej2a,I,err,mit)
print(hx)
print(hy)
######################################################
"""
I = [1,2]
err = 10**-5
mit = 100

hx, hy = lab2eje1.rbisec(fun_lab2ej2b,I,err,mit)
print(hx)
print(hy)
"""
######################################################