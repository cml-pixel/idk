# modificat stock
#vender productos
import os,time,csv

print(f"bienvenido al sistema de gestion de verduras, don felipes")

usuariocuenta="vendedor"
contraseñausuario="1234"

while True:
    usuario=input("ingrese usuario >")
    contraseña=input("ingrese contraseña >")
    if usuario==usuariocuenta and contraseña==contraseñausuario:
        print("ha ingresado con exito")
        time.sleep(1)
        os.system('cls')
        break
    else:
        print(f"usuario o contraseña incorrecta")
        time.sleep(1.5)
        os.system('cls')
        
stock={}
opcionmenu=4
while opcionmenu !=3:
    print(f"1.- agregar stock")
    print(f"2.- vender")
    print(f"3.- salir")
    opcionmenu=int(input("ingrese la opcion que desea  >"))

    match opcionmenu:
        case 1:
            print("debe ingresar el stck correspondiente a la verduderia")
            nomproducto=input("ingrese el nombre del producto > ")
            valorroducto=int(input("ingrese el valor del producto > "))
            cantidadroducto=int(input("ingrese la cantidad del producto > "))
            
            with open('registro_verduderia.csv','w+', newline='') as registro:
                escritor=csv.writer(registro)
                lector=csv.reader(registro)
                matrizalmacen=[[]]
                for fila in lector:
                    matrizalmacen.append(fila)
                escritor.append([nomproducto,valorroducto,cantidadroducto])
                escritor.writerows(matrizalmacen)
