#Tomado y adaptado de: https://gist.github.com/pedrojimenezp/4683242
print("------- Interpolacion Polinomica (Newton) -------")
#Grado del polinomio
n = 4

matriz = [0.0] * n
for i in range(n):
    matriz[i] = [0.0] * n

vector = [0.0] * n

#x = [0,1,3,6]
#y = [-3,0,5,7]
x = [1,5,20,40]
y = [56.5,113,181,214.5]

#print matriz
#print vector
for i in range(n):
    vector[i]=x[i]
    matriz[i][0]=y[i]

#print("vector: ")
#print(vector)
#print("matriz: ")
#print(matriz)
punto_a_evaluar = 2

for i in range(1,n):
    for j in range(i,n):
        matriz[j][i] = ((matriz[j][i-1]-matriz[j-1][i-1]) / (vector[j]-vector[j-i]))
        #print("matriz[",j,"][",i,"] = ",(matriz[j][i-1]-matriz[j-1][i-1])/(vector[j]-vector[j-i]))

#print("Matriz de multiplicacion: ")
#print(matriz)

aprx = 0
mul = 1.0
for i in range(n):
    #print("matriz[",i,"][",i,"]","=",matriz[i][i])
    mul = matriz[i][i];
    #print("mul antes del ciclo j=",mul)
    for j in range(1,i+1):
        mul = mul * (punto_a_evaluar - vector[j-1])
        #print("mul en el ciclo j=",mul)
    # print aprx
    aprx = aprx + mul


print(aprx)
#print("El valor aproximado de f(",punto_a_evaluar,") es: ", aprx)