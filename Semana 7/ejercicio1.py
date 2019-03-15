#Creado por:Efren Jimenez
#Fecha:14/03/2019
#Objetivo: Ejercicio 1

def IngresarPalabra():
    lista = []
    cantidadPalabras = int(input("Digite la cantidad a palabras a ingresar"))
    contador = 0
    while contador < cantidadPalabras:
        lista.append(input("Digite la palabra"))
        contador =contador+1

    for item in lista[::-1]:
        print(item)

IngresarPalabra()