# laboratorio 6 - ejercicio 1
import numpy as np

def jacobi(A,b,err,mit):
    M = np.diag(np.diag(A))
    N = M - A
    Minv = np.diag(1/np.diag(M))
    x_old = np.zeros(b.shape)
    for k in range(mit):
        x_new = Minv @ ( N @ x0 ) + Minv @ b
        if np.linalg.norm(x_new-x_old, ord=np.inf) <= err:
            break
        else:
            x_old = x_new.copy()
    return [x1,k+1]
'''
def jacobi(A, b, err, mit):
    n = A.shape[0]
    x = np.zeros(n)
    x_n = np.zeros(n)
    for k in range(mit):
        for i in range(n):
            suma = 0
            for j in range(n):
                if j!=i:
                    suma = suma + A[i,j] * x[j]         
            x_n[i] = (b[i] - suma)/ A[i,i]
        if np.linalg.norm(x_n - x, np.inf) <= err:
            return x_n, k+1   
        x = x_n.copy() 
    return [x,k+1]
'''
def gseidel(A, b, err, mit):
    n = A.shape[0]
    x = np.zeros(n)
    x_n = np.zeros(n)

    for k in range(mit):
        for i in range(n):
            suma = 0
            for j in range(n):
                if j!=i:
                    suma = suma + A[i,j] * x_n[j]
            x_n[i] = (b[i] - suma)/ A[i,i]
        if np.linalg.norm(x_n - x, np.inf) <= err:
            return x_n, k+1 
        
        x = x_n.copy() 
    return [x, k+1]
