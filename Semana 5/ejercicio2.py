numero=int(input("Digite un numero"))
mayor=numero
menor=numero

while numero>=0:
    print(numero)
    numero = int(input("Digite un numero"))
    if numero>mayor:
        mayor=numero
    if numero<menor and numero>0:
        menor=numero

print("El numero menor es ",menor)
print("El numero mayor es ",mayor)
print("Gracias por usar el mejor programa"
      "a los morados no ")