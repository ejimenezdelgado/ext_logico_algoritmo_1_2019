# Fecha:14/02/2019
# Creado por:Efrén Jiménez
# Objetivo:Realizar el ejercicio 2

# Crear las variables
parcial1=0
parcial2=0
parcial3=0
enClase1=0
enClase2=0
final=0
promedio=0


parcial1 = int(input("Digite la nota del parcial 1"))
parcial2 = int(input("Digite la nota del parcial 2"))
parcial3 = int(input("Digite la nota del parcial 3"))

porcentajeTotalParciales=\
    int(input("Cual es el porcentaje de los parciales"))

porcentajeParciales=(porcentajeTotalParciales/3)/100

porcentajeParcial1=parcial1 * porcentajeParciales
porcentajeParcial2=parcial2 * porcentajeParciales
porcentajeParcial3=parcial3 * porcentajeParciales


enClase1 = int(input("Digite la nota del trabajo clase 1"))
enClase2 = int(input("Digite la nota del trabajo clase 2"))

porcentajeEnClaseTotal=\
    int(input("Cual es el porcentaje de los trabajos en clase"))

porcentajeEnClase=(porcentajeEnClaseTotal/2)/100

porcentajeEnClase1=enClase1 * porcentajeEnClase
porcentajeEnClase2=enClase2 * porcentajeEnClase


final=int(input("Digite la nota del trabajo final"))

porcentajeTrabajoFinalTotal=\
    int(input("Cual es el porcentaje del trabajo final"))

porcentajeTrabajoFinal=final * (porcentajeTrabajoFinalTotal)/100

promedio=porcentajeParcial1+porcentajeParcial2+porcentajeParcial3+porcentajeEnClase1+porcentajeEnClase2+porcentajeTrabajoFinal

print("La nota del parcial 1 es ",parcial1)
print("La nota del parcial 2 es ",parcial2)
print("La nota del parcial 3 es ",parcial3)
print("La nota del trabajo en clase 1 es ",enClase1)
print("La nota del trabajo en clase 2 es ",enClase2)
print("La nota del trabajo final es ",final)
print("El promedio final es ",promedio)