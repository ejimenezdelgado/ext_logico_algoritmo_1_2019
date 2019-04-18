
def NumeroPrimo(numero):
    esPrimillo=False
    contador=1
    divisores=0
    while contador<=numero:
        if numero%contador==0:
            divisores=divisores+1
        contador = contador + 1
    if divisores==2:
        esPrimillo=True

    return esPrimillo

def Recorrido():
    listaPrimos=[]
    for i in range(1,1001):
        if NumeroPrimo(i)==True:
            listaPrimos.append(i)
    return listaPrimos

def Imprimir():
    lista=Recorrido()
    for valorNumeral in lista:
        print(valorNumeral)

Imprimir()