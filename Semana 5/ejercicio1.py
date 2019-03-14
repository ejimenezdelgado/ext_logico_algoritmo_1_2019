
numero=int(input("Digite un numero"))

while numero<0 or numero >10:

    print("Este numero no funciona, "
          "digitelo de nuevo un numero "
          "entre 0 y 10", numero)
    numero = int(input("Digite un numero"))

print("El numero de la loteria es", numero)