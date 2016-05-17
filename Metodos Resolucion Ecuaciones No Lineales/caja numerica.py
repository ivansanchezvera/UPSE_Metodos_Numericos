#Creado en base a:
#Rodriguez Ojeda, L. (2015). Analisis Numerico Basico. Guayaquil: ESCUELA POLITECNICA DEL LITORAL (ESPOL).

from sympy import*
x = Symbol('x')
f = 250-(192*x) + (28*x**2) - x**3
r = solve(f)
#vemos que r es un vector con 3 soluciones
len(r)

print(r[0].evalf(10))
print(r[1].evalf(10))
print(r[2].evalf(10))
