#Creado por:Efrén Jiménez
#Fecha:07/03/2019
#Objetivo: Ejercicio1

nota=0
contador=1
sumatoria=0
promedio=0


while contador<=5:
    nota=int(input("Digite la nota "+str(contador)))
    sumatoria=sumatoria+nota
    contador=contador+1
promedio=sumatoria/5
print("El promedio es",promedio)
