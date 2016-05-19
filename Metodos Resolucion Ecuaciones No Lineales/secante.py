import sys
from pylab import*

def f(x):
    #return e**-x - x
    return x ** 3 + 2 * x**2 + 10 * x - 20

#Definiendo el metodo de la secante
def secante(x0, x1, maxIter):
    for i in range(maxIter):
        #Paro cuando llego a la respuesta
        if f(x1) - f(x0) == 0:
            return x1
        x_temp = x1 - (f(x1) * (x0 - x1) ) / (f(x0) - f(x1))
        x0 = x1
        x1 = x_temp
    #Paro cuando se cumple el numero de iteraciones maximo
    return x1

x0 = 0
x1 = 1
maxIter = 10
raiz = secante(x0,x1,maxIter)

print(raiz)
xPrintLeft = raiz - x0-(x1-x0)/2
xPrintRight = raiz + x1+(x1-x0)/2
xRate = (x1-x0)/20

x = arange(xPrintLeft,xPrintRight,xRate)
#f = 250-(192*x) + (28*x**2) - x**3
plot(x,f(x))
grid(True)
show()