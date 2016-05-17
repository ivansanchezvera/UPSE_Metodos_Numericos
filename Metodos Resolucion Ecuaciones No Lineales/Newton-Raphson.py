def newton(f, df, x_0, maxiter=50, xtol=1.0e-6, ftol=1.0e-6):
    """Método de Newton
    Halla la raíz de la función f en el entorno de x_0 mediante el método de
    Newton.
    Argumentos
    ----------
    f - Función
    df - Función, debe ser la función derivada de f
    x_0 - Punto de partida del método
    maxiter (opcional) - Número máximo de iteraciones
    xtol (opcional) - Cota para el error relativo para la raíz
    ftol (opcional) - Cota para el valor de la función
    Devuelve
    --------
    x - Raíz de la ecuación en el entorno de x_0
    Excepciones
    -----------
    RuntimeError - No hubo convergencia superado el número máximo de
                   iteraciones
    ZeroDivisionError - La derivada se anuló en algún punto
    Exception - El valor de x se sale del dominio de definición de f
    Ejemplos
    --------
    >>> def f(x): return x ** 2 - 1
    ...
    >>> def df(x): return 2 * x
    ...
    >>> newton(f, df, 2)
    1.000000000000001
    >>> newton(f, df, 5)
    1.0
    >>> newton(f, df, 0)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "ceros.py", line 102, in newton
        dx = -f(x) / df(x)  # ¡Aquí se puede producir una división por cero!
    ZeroDivisionError: float division by zero
    """
    x = float(x_0)  # Se convierte a número de coma flotante
    for i in xrange(maxiter):
        dx = -f(x) / df(x)  # ¡Aquí se puede producir una división por cero!
                            # También x puede haber quedado fuera del dominio
        x = x + dx
        if abs(dx / x) < xtol and abs(f(x)) < ftol:
            return x
    raise RuntimeError("No hubo convergencia después de {} iteraciones".format(maxiter))