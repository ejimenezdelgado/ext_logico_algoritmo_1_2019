#Creado por:Efrén Jiménez
#Fecha:07/03/2019
#Objetivo: Ejercicio3

contador=10
numeroDecimal=0
numeroUnidad=0
while contador<=100:
    numeroDecimal=contador//10
    numeroUnidad=contador-(numeroDecimal*10)
    if numeroDecimal==numeroUnidad:
        print("Este numero es palindromo",contador)
    contador=contador+1