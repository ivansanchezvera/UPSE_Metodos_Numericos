#Creado en base a:
#Rodriguez Ojeda, L. (2015). Analisis Numerico Basico. Guayaquil: ESCUELA POLITECNICA DEL LITORAL (ESPOL).

from pylab import*
#Arange devuelve un arreglo con numeros desde el elemento de inicio (primer parametro)
#hasta el elemento final (segundo parametro) avanzando segun el 3er parametro
x = arange(0.5,1.5,0.05)
#f = 250-(192*x) + (28*x**2) - x**3
f = x**3 + 2*x**2 + 10*x - 20
plot(x,f)
grid(True)
show()