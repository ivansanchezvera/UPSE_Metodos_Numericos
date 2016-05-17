import numpy as np
def biseccion(f, a, b, tol=1.0e-6):
    """Método de bisección
    Halla una raíz de la función f en el intervalo [a, b] mediante el método
    de bisección.
    Argumentos
    ----------
    f - Función, debe ser tal que f(a) f(b) < 0
    a - Extremo inferior del intervalo
    b - Extremo superior del intervalo
    tol (opcional) - Cota para el error absoluto de la x
    Devuelve
    --------
    x - Raíz de f en [a, b]
    Excepciones
    -----------
    ValueError - Intervalo mal definido, la función no cambia de signo en el
                 intervalo o cota no positiva
    Ejemplos
    --------
    >>> def f(x): return x ** 2 - 1
    ...
    >>> biseccion(f, 0, 2)
    1.0
    >>> biseccion(f, 0, 5)
    1.000000238418579
    >>> biseccion(f, -2, 2)
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "ceros.py", line 35, in biseccion
        raise ValueError("La función debe cambiar de signo en el intervalo")
    ValueError: La función debe cambiar de signo en el intervalo
    >>> biseccion(f, -3, 0, tol=1.0e-12)
    -1.0000000000004547
    """
    if a > b:
        raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0.0:
        raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")
    x = (a + b) / 2.0
    i = 0
    while True:
        i = i+1
        print(i)
        if b - a < tol:
            return x
        # Utilizamos la función signo para evitar errores de precisión
        elif np.sign(f(a)) * np.sign(f(x)) > 0:
            a = x
        else:
            b = x
        x = (a + b) / 2.0

def f(x): return ((x**3) + (x) - (1))
sol = biseccion(f, 0, 1)
print(sol)