#Calcula la probabilidad condicional P(x|y) a partir de la frecuencia relativa
#de n experimentos

#Importa el modulo de aleatorios
from random import randint

# Conjunto X
Xmin = 0
Xmax = 3

# Conjunto Y
Ymin = 2
Ymax = 4

#Minimo y máximo del intervalo completo
if (Xmin <= Ymin) : minIntervalo = Xmin #Determina el elemento mínimo
else              : minIntervalo = Ymin

if (Xmax >= Ymax) : maxIntervalo = Xmax #Determina el elemento máximo
else              : maxIntervalo = Ymax

#Bandera que indica que hay intersección
bandIntersec = 1

#Intersección
if (Xmin <= Ymin): minInterseccion = Ymin
else             : minInterseccion = Xmin

if (Xmax <= Ymax): maxInterseccion = Xmax
else             : maxInterseccion = Ymax

if minInterseccion > maxInterseccion: bandIntersec = 0

#Elemento x con el que se calculará la frecuencia relativa
x = 3

#Elemento y con el que se calculará la frecuencia relativa
y = 3

#Cantidad de experimentos
n = 100000

#Código de error
error = 0

#Contador que determina que fue un evento simultaneo
contXY = 0

#Contador de las veces que el evento pertenece a Y
contY = 0

#Verificación de error
if   Xmin > Xmax             : error = 1 #Error de rango de X o de Y
elif Ymin > Ymax             : error = 1
elif (x < Xmin) or (x > Xmax): error = 2 #x mo pertenece a X
elif (y < Ymin) or (y > Ymax): error = 2 #y mo pertenece a Y
elif n <= 0                  : error = 3 #Error en la cantidad de experimentos
else:
    for i in range(n):
        aleatorio = randint(minIntervalo,maxIntervalo)
        if (aleatorio >= Ymin) and (aleatorio <= Ymax): contY +=1
        if bandIntersec == 1:
            if (aleatorio >= minInterseccion) and (aleatorio <= maxInterseccion):
                contXY +=1

#Imprime el error
if error != 0  : print("Error: ",error)
elif contY > 0 : print("Probabilidad condicional de x = ",x,"y y =: ",y," : ",
                      contXY/contY) #Frecuencia relativa
else           : print("La probabilidad no se puede calcular")
