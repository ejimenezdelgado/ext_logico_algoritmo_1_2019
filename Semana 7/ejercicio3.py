#Creado por:Efren Jimenez
#Fecha:14/03/2019
#Objetivo: Ejercicio 3


def IngresarPalabra():
    lista=[]
    listaInvertida=[]
    cantidadPalabras=int(input("Digite la cantidad a palabras a ingresar"))
    contador=0
    while contador < cantidadPalabras:
        lista.append(input("Digite la palabra"))
        contador = contador+1
    contador = cantidadPalabras - 1
    len(lista)
    while contador >= 0:
        listaInvertida.append(lista[contador])
        contador -= 1
    print("La lista es :", lista)
    print("La invertida es :", listaInvertida)

IngresarPalabra()