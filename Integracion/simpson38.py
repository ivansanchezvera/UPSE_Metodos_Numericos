#Tomado de: http://rodrigogr.com/blog/metodo-de-integracion-simpson-13/
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Importamos math
from math import *

#Definimos la funcion
#@ n: numero de x
#@ a y b los intervalos de la integral
#@ f: La funcion a integrar
def simpson38(n, a, b, f):

    #validamos
    if(n%3!=0):
        raise ValueError('N debe ser multiplo de 3.')

    #calculamos h
    h = (b - a) / n
    #Inicializamos nuestra varible donde se almacenara las sumas
    suma = 0.0
    #hacemos un ciclo para ir sumando las areas
    for i in range(1, n):
        #calculamos la x
        #x = a - h + (2 * h * i)
        x = a + i * h
        # si es par se multiplica por 4
        if(i % 3 == 0):
            suma = suma + 2 * fx(x, f)
        #en caso contrario se multiplica por 2
        else:
            suma = suma + 3 * fx(x, f)
    #sumamos los el primer elemento y el ultimo
    suma = suma + fx(a, f) + fx(b, f)
    #Multiplicamos por h/3
    rest = suma * (3*h / 8)
    #Retornamos el resultado
    return (rest)

#Funcion que nos ayuda a evaluar las funciones
def fx(x, f):
    return eval(f)

#valores de ejemplo para la funcion sin(x) con intervalos de
n = 6
a = 0.0
b = 1.0
#f = '(x+1)**-1'
#f = 'x*(e**(3*x))'
n = 9
a = 0
b = 0.8
f = '0.2+25*x-200*(x**2)+675*(x**3)-900*(x**4)+400*(x**5)'

print(simpson38(n, a, b, f))