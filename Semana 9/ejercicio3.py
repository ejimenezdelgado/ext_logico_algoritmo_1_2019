
#Creado por:Efrén Jiménez
#Fecha:28/03/2019
#Objetivo: Ejercicio 2


def NumerCercano():
    contador=0
    menor=0
    numeroUno = int(input("Digite un numero"))
    diferencia=-1
    while contador<4:
        numero=int(input("Digite un numero"))
        resultado=numero[contador]-numeroUno[0]
        if resultado<diferencia or diferencia ==-1:
            diferencia=resultado
            menor=numero
        contador=contador+1
    print("El numero mas cercano es",menor)

NumerCercano()



