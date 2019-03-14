#Creado por Efrén Jiménez
#Fecha:21/02/2019
#objetivo: Ejercicio1

def Imprimir():
    print("Bienvenidos al mejor "
          "curso de programacion del mundo :)")

def ProcesoNumeros():
    contador=1
    while contador<=25:
        if contador%2==0:
            print(contador)
        contador=contador+1

Imprimir()
ProcesoNumeros()