# laboratorio 2 - ejercicio 3
def rnewton(fun, x0, err, mit):
    hx = [x0]
    hf = [fun(x0)[0]]

    for k in range(1, mit+1):
        x_prev = hx[-1]
        f_x, f_prime_x = fun(x_prev)
        
        if abs(f_prime_x) < 1e-15:
            break
        
        x_next = x_prev - f_x / f_prime_x
        hx.append(x_next)
        hf.append(fun(x_next)[0])

        if abs(x_next - x_prev) / abs(x_next) < err or abs(f_x) < err or k >= mit:
            break

    return hx, hf