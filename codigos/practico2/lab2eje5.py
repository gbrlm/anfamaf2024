# laboratorio 2 - ejercicio 5
def ripf(fun, x0, err, mit):
    hx = [x0]
    for k in range(1, mit + 1):
        x0 = hx[-1]
        xn = fun(x0)
        hx.append(xn)

        if abs(xn - x0) < err or k >= mit:
            break

    return hx
