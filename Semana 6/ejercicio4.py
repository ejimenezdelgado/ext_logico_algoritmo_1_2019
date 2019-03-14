#Creado por:Efrén Jiménez
#Fecha:07/03/2019
#Objetivo: Ejercicio4

contador=1
sumaDivisores=0

numero=int(input("Digite un numerito perpetirifillo"))

while contador<numero:
    if numero%contador==0:
        sumaDivisores=sumaDivisores+contador
    contador = contador + 1
if numero==sumaDivisores:
    print("Este numero numerito perpetirifillo ",contador)
else:
    print("Este numero numerito no es perpetirifillo")