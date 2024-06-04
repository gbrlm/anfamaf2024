# laboratorio 5 - ejercicio 1

import numpy as np

def intenumcomp(f,a,b,N,regla):
    x = np.linspace(a,b,N+1)
    f = np.array([f(xi) for xi in x])
    h = (b-a)/N
    if regla == "trapecio":        
        S = (h/2)*(f[0] + 2 * sum(f[1:-1]) + f[-1])
    elif regla == "pm":
        if N%2 != 0: 
            # esto es que hay una cantidad impares de intervalos
            print("Se necesita una cantindad de intervalos (N) par")
            return None
        S = h*2*np.sum(f[1::2])
    elif regla == "simpson":
        if N%2 != 0:
            print("Se necesita una cantindad de intervalos (N) par")
            return None
        
        """
        f0 = f[0]
        fn = f[-1]
        f = np.reshape(f[:-1],(-1,2))
        f_pares = f[1:,0]
        f_impares = f[:,1]
        """
        f_pares = f[::2]
        f0 = f[0]
        fn = f[-1]
        f_pares = f_pares[1:-1]
        f_impares = f[1::2]
                
        
        S = (h/3)*(f0 + 2 * np.sum(f_pares) + 4*np.sum(f_impares) +  fn)
    else:
        print("La regla no es válida")
        return None
    return S

'''
def  fun(x):
    return np.exp(-x)

def test_integracion():
    print(intenumcomp(fun,0,1,100,"pm"))
    print(intenumcomp(fun,0,1,100,"trapecio"))
    print(intenumcomp(fun,0,1,18,"simpson"))
    
    
err = np.inf  
N = 0
it = 0
regla = "simpson" 
while err>1e-8:
    it = it + 1
    N = N + 2
    I = intenumcomp(fun,0,1,N,regla)
    err = abs(I - (-np.exp(-1)+1))
    print(I,err, it)
'''