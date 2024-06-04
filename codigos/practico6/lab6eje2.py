import numpy as np
from lab6eje1 import jacobi, gseidel

A1 = np.array([3,1,1,2,6,1,1,1,4], dtype=float).reshape(3,3)
b1 = np.array([5, 9, 6], dtype=float)

A2 = np.array([5,7,6,5,7,10,8,7,6,8,10,9,5,7,9,10], dtype=float).reshape(4,4)
b2 = np.array([23,32,33,31], dtype=float)

tol1 = 1e-11
tol2 = 1e-4
mit1 = 100
mit2 = 10000

sol_1_j = jacobi(A1,b1,1e-11,100)
sol_1_g = gseidel(A1, b1, 1e-11, 100)

sol_2_j = jacobi(A2, b2, 1e-4, 10000)    
sol_2_g = gseidel(A2, b2, 1e-4, 10000)

if sol_1_j[1] < mit1:
    print(f'El método de Jacobi converge a la solución del problema 1 {sol_1_j[0]} en {sol_1_j[1]} iteraciones')
else:
    print(f'El método de Jacobi llegó al máximo de iteraciones para el problema 1 en {sol_1_j[0]}')

if sol_1_g[1] < mit1:
    print(f'El método de Gauss-Seidel converge a la solución del problema 1 {sol_1_g[0]} en {sol_1_g[1]} iteraciones')
else:
    print(f'El método de Gauss-Seidel llegó al máximo de iteraciones para el problema 1 en {sol_1_g[0]}')


if sol_2_j[1] < mit2:
    print(f'El método de Jacobi converge a la solución del problema 2 {sol_2_j[0]} en {sol_2_j[1]} iteraciones')
else:
    print(f'El método de Jacobi llegó al máximo de iteraciones para el problema 2 en {sol_2_j[0]}')

if sol_2_g[1] < mit2:
    print(f'El método de Gauss-Seidel converge a la solución del problema 2 {sol_2_g[0]} en {sol_2_g[1]} iteraciones')
else:
    print(f'El método de Gauss-Seidel llegó al máximo de iteraciones para el problema 2 en {sol_2_g[0]}')
