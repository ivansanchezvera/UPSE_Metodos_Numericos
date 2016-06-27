from pylab import*
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#r = eval(input("Ingresa el valor del grado r: "))
#x = list(eval(input("Ingrese los valores de X separados por comas: ")))
#y = list(eval(input('Ingrese los valores de Y separados por comas : ')))
#X = float(eval(input(' Ingrese el valor de px: ')))
'''
r = 3
#x = [1,5,20,40]
x = [0,1,3,6]
y = [-3,0,5,7]
#y = [56.5,113.0,181.0,214.5]
#X = 2
X = 1.8

px = 0
for i in range(r + 1):
    l = y[i]
    for j in range(r + 1):
        if j != i:
            l = l * ((X - x[j]) / (x[i] - x[j]))
    px = px + l
print (px)

#f = 3*x*e**x
plot(x,y)
grid(True)
show()