#Based on: / Tomado de: http://programmers.stackexchange.com/questions/185705/computing-integration-with-the-trapezoidal-rule

from __future__ import division

def trapezoidal_rule(f, a, b, n):
    """Approximates the definite integral of f from a to b by
    the composite trapezoidal rule, using n subintervals"""
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += 2 * f(a + i * h)
    return s * h / 2

integral = trapezoidal_rule(lambda x:3*x, 1, 2, 10)
print(integral)

# displays 1000000000.75