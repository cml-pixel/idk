#trabajo

import csv
empresasPequeñas={}
empresasMediana={}
empresasGrande={}

clasificacionEmpresa=["Pequeño Contribuyente","Mediano Contribuyente","Gran Contribuyente"]

while True:
    print("1) Imprimir pequeñas contribuyentes")
    print(" ")
    print("2) Imprimir medianas contribuyentes")
    print(" ")
    print("3) Imprimir Grandes contribuyentes")
    print(" ")
    print("4) Exportar contribuyentes")
    print(" ")
    print("5) Salir")
    print(" ")
    
    opcionMenu=int(input("Ingresar opción > "))
    
    match opcionMenu:
        case 1:
            with open('listadoRutEmpresa.csv','r') as archivo_empresas:
                lector_csv=csv.DictReader(archivo_empresas)
                for fila in lector_csv:
                    venta=int(fila["ventas"])
                    if venta < 100000000:
                        ultimaClave=len(empresasPequeñas)+1
                        empresasPequeñas[ultimaClave]=fila
                for clave in empresasPequeñas:
                    print(empresasPequeñas[clave])
        case 2:
            with open('listadoRutEmpresa.csv','r') as archivo_empresas:
                lector_csv=csv.DictReader(archivo_empresas)
                for fila in lector_csv:
                    venta=int(fila["ventas"])
                    if venta > 100000000 and venta <= 200000000:
                        ultimaClave=len(empresasMediana)+1
                        empresasMediana[ultimaClave]=fila
                for clave in empresasMediana:
                    print(empresasMediana[clave])
        case 3:
            with open('listadoRutEmpresa.csv','r') as archivo_empresas:
                lector_csv=csv.DictReader(archivo_empresas)
                for fila in lector_csv:
                    venta=int(fila["ventas"])
                    if venta > 200000000:
                        ultimaClave=len(empresasGrande)+1
                        empresasGrande[ultimaClave]=fila
                for clave in empresasGrande:
                    print(empresasGrande[clave])
        case 4:
            break
        case 5:
            print("Hasta pronto!")