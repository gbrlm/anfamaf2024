import lab2eje1
import lab2eje3
import lab2eje5
import math

def lab2ej7bisec(x):
	# calcula u(x) = y
	fun_auxiliar = lambda y : y - math.exp(-(1-x*y)**2)
	"""
	usar lambda es como hacer:
	def u(y):
		return y - math.exp(-(1-x*y)**2)
	
	"""
	hy, hu = lab2eje1.rbisec(fun_auxiliar, [0.0,2.0], 1e-6, 100)
	y = hy[-1]
	return y

def lab2ej7newton(x):
	# calcula u(x) = y
	fun_auxiliar = lambda y : (y - math.exp(-(1-x*y)**2), \
		1 - math.exp(-(1-x*y)**2)*(-2*(1-x*y)*(-x)))
	hy, hu = lab2eje3.rnewton(fun_auxiliar, 1.0, 1e-6, 100)
	y = hy[-1]
	return y

def lab2ej7ipf(x):
	# calcula u(x) = y
	fun_auxiliar = lambda y : math.exp(-(1-x*y)**2)
	hy = lab2eje5.ripf(fun_auxiliar, 1.0, 1e-6, 100)
	y = hy[-1]
	return y

