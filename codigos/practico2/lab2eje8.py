from lab2eje3 import rnewton
import math
import matplotlib.pyplot as plt

def fun(x):
    return math.tan(x) / x ** 2

def der_fun(x):
    f = 1 / (math.cos(x) * x) ** 2 - 2 * math.tan(x) / x ** 3
    df = (6 * math.tan(x) + 2 * x * (x * math.tan(x) - 2) * (math.cos(x) ** -2)) / x ** 4
    return f, df

hx, hf = rnewton(der_fun, 1.0, 1e-5, 100)
print(f"El método encontró el mínimo en {len(hx)} iteraciones")

x = [i * 2 * math.pi / 1000 for i in range(100, 200)]
y = [fun(xi) for xi in x]

plt.plot(x, y, linewidth=2, label = "tan(x)")
plt.plot(hx[-1], fun(hx[-1]), '*', markersize=25)
plt.legend()
plt.show()
