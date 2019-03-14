#Creado por:Efrén Jiménez
#Fecha:07/03/2019
#Objetivo: Ejercicio2

menor=0
mcd=0
contador=1
numero1=int(input("Digite el numero 1"))
numero2=int(input("Digite el numero 2"))

if numero1<numero2:
    menor=numero1
else:
    menor=numero2

while contador<menor:
    if numero1%contador==0 and numero2%contador==0:
        mcd=contador
    contador=contador+1
print("El MCD es ", mcd)
