def resta(a,b):
    return a-b

def resta (a,b):
    return a-b

def funcion():
    return "Bienvenidos a python"

frase = funcion()
print(frase)

def resta(a=None, b=None):
    if a==None or b==None:
        print("Error, faltan parámeros a la función")
        return
    return a-b
resta()

def calculo(precio,descuento):
    return precio-(precio*descuento/100)

datos=[10000,10]
print("El monto final a pagar es: ", calculo(*datos))

def saludo(nombre, mensaje='Python'):
    print(mensaje, nombre)
    
saludo(mensaje="Buen día", nombre="Pedro")