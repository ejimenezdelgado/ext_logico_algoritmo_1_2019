
lista=[]
numeroValores=0

def Solicitar():
    numeroValores=int(input("Digite el numero de valores que desea agregar"))
    return numeroValores

def LLenar(numeroValores):
    for numerito in range(0,numeroValores):
        lista.append(int(input("Digite un numero")))

def Ciclo():
    contador=0
    cumple = 0
    while contador<numeroValores:

        if contador%2==0:
            if lista[contador]>lista[contador+1]:
                cumple=0
            else:
                cumple=1
                break
        if contador+1==len(lista):
            break
        contador=contador+1
    Decision(cumple)

def Decision(crudaDecision):
    if crudaDecision==0:
        print("La lista es partidaria")
    else:
        print("La lista no es partidaria")

numeroValores=Solicitar()
LLenar(numeroValores)
Ciclo()

