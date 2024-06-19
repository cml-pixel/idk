def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    try:
        resultado=a/b
    except ZeroDivisionError:
        return "NO SE PUEDE DIVIDIR POR 0"
    else:
        return a/b

def validar_numero(numero):
    try:
        numeroFloat=float(numero)
    except:
        print("El valor no es un número")
        
while True:
    print(" ")
    a=int(input("Ingrese un número: "))
    print(" ")
    b=int(input("Ingrese otro número: "))

    print(" ")
    print("Elija lo que quiere hacer: ")
    print(" ")
    print("1) Suma")
    print(" ")
    print("2) Resta")
    print(" ")
    print("3) Multiplicación")
    print(" ")
    print("4) División")
    print(" ")
    print("5) Salir")
    print(" ")
    opc=int(input("Opción: "))

    match opc:
        case 1:
            print("El resultado es: ",suma(a,b))
        case 2:
            print("El resultado es: ",resta(a,b))
        case 3:
            print("El resultado es: ",multiplicacion(a,b))
        case 4:
            print("El resultado es: ", division(a,b))
        
        case 5:
            print("Adiós")
            break