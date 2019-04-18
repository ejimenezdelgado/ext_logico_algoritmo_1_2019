
#Creado por:Efrén Jiménez
#Fecha:28/03/2019
#Objetivo: Ejercicio 3


def NumerCercano():
    contador=1
    menor=0
    lista=[]
    for variable in range(0,5):
        lista.append(int(input("Digite un numero")))
    diferencia=-1
    while contador<4:
        resultado=lista[contador]-lista[0]
        if resultado<diferencia or diferencia ==-1:
            diferencia=resultado
            menor=lista[contador]
        contador=contador+1
    print("El numero mas cercano es",menor)
NumerCercano()



