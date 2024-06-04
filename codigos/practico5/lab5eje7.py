import numpy as np

def simple(fun,a,b):
	return (b-a)/6 * (fun(a) + 4 *fun((a+b)/2) + f(b))

def recursiva(fun,a,b,err):
	c = (a+b)/2
	q = simpson(fun,a,b)
	q1 = simpson(fun,a,c)
	q2 = simpson(fun,c,b)
	if abs(q-q1-q2) < 15*err:
		I = q1 + q2
	else:
		q1 = recursiva(fun,a,c,err/2)
		q2 = recursiva(fun,c,b,err/2)
		I = q1 + q2
	return I

def fun(x):
	np.sin(x)

xx = np.linspace(0, np.pi/2, 100)
yy = np.sin(xx)

integral = recursiva(fun, 0, np.pi/2, 1e-6)
print(integral)
