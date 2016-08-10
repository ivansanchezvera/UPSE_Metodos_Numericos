from __future__ import division

def trapecio_tabla(f, X, a, b, n):
    """Approximates the definite integral of f from a to b by
    the composite trapezoidal rule, using n subintervals"""
    if(len(f)!=len(X)):
        print("Error no se puede ejecutar el metodo. Arreglos deben ser del mismo tamano")
        return -1

    h = (b - a) / n
    #Comprobamos las diferencias
    for i in range(1, len(X)):
        dx = X[i] - X[i-1]
        if (dx) - h > 0.000001:
            print("Error no se puede ejecutar el metodo. Diferencias entre valores de x no coinciden")
            return -1

    s = valoresfx[0] + valoresfx[len(valoresfx)-1]
    for i in range(1, n):
        s += 2 * f[i]
    return s * h / 2

valoresX = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
valoresfx = [1,7,4,3,5,2]
integral = trapecio_tabla(valoresfx, valoresX, valoresX[0], valoresX[len(valoresfx)-1], len(valoresfx)-1)
print(integral)

# displays 1000000000.75