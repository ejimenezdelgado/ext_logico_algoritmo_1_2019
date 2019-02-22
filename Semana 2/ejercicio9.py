#Creado por:Efrén Jiménez
#Fecha:21/02/2019
#Objetivo: Ejercicio9

precioEntrada=0
cantidadEntradas=0
descuento=0
precio=0
nuevoPrecio=0

precioEntrada= int(input("Digite un el precio de la entrada"))
cantidadEntradas= \
    int(input("Digite ula cantidad de entradas a comprar"))

precio=precioEntrada*cantidadEntradas

if cantidadEntradas==1:
    print("No sea cochino pague")

if cantidadEntradas==2:
    descuento=(5/100)

if cantidadEntradas==3:
    descuento=(7/100)

if cantidadEntradas==4:
    descuento=(10/100)

nuevoPrecio=precio-(precio*descuento)

print("El total de entradas es ",cantidadEntradas)
print("El precio total original es ",precio)
print("El precio total con descuento es ",nuevoPrecio)
print("El descuento fue de ",(precio*descuento))
print("El porcentaje de decuento fue de ",descuento)