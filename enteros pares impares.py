def validar_lista_numeros():
    numerosEnteros=[]
    while True:
        
        try:
            numeros=input("Ingrese numeros separados por espacio: ")
            strNumeros=numeros.split()
            for numero in strNumeros:
                numerosEnteros.append(int(numero))
        except ValueError:
            print("Ingrese números separados por espacios")
            numerosEnteros.clear()
        else:
            return numerosEnteros
        
def numeros_pares(numeros):
    pares=[]
    for numero in numeros:
        if numero%2==0:
            pares.append(numero)
    return pares
    
def numeros_impares(numeros):
    impares=[]
    for numero in numeros:
        if numero%2!=0:
            impares.append(numero)
    return impares

listaNumeros=validar_lista_numeros()
listaImpares=numeros_impares(listaNumeros)
listaPares=numeros_pares(listaNumeros)
print("Números ingresados:",listaNumeros)
print("Numeros pares:" ,listaPares)
print("Números impares:" ,listaImpares)