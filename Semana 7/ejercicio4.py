#Creado por:Efren Jimenez
#Fecha:14/03/2019
#Objetivo: Ejercicio 4

def Suma():
    lista=[]
    listaSuma = []
    suma=0
    numero=int(input("Digite el numero de elementos"))
    for insertar in range(1,numero+1):
        lista.append(int(input("Digite un numero")))
    for sumita in lista:
        suma=suma+sumita
        listaSuma.append(suma)
        print(suma)
    print("La suma total es", suma,listaSuma)

Suma()