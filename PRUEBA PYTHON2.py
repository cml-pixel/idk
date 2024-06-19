#Pruebalol

#MOBBUS99

userValido="vendedor"
contrValida=12345

print("Bienvenido al sistema de venta de pasajes MOBBUS99!")
print(" ")
while True:
    print("Por favor, inicie sesión con el usuario y contraseña correctos")
    print(" ")
    usuario=input("Usuario:  ")
    contrasenia=int(input("Contraseña:  "))
    
    if usuario==userValido and contrasenia==contrValida:
        print("Inicio de sesion correcto! redireccionando")
        print(" ")
        break
    else:
        print("El usuario o contraseña ingresados no son correctos, verifique")
#
print(f"Bienvenido {usuario}!")
print(" ")

viajes=[]

while True:
    print("Seleccione la opción que desee")
    print(" ")
    print("1) Generar pasaje")
    print("2) Vender pasaje")
    print("3) Cerrar Caja")
    print("4) Salir")
    print(" ")
    opc=int(input("Seleccione:  "))
    
    if opc==1:
        print(" ")
        print("Los destinos son los siguientes")
        print(" ")
        print("1) Valparaíso | Días hábiles: $5000 | Sábado-Domingo: $6000")
        print("2) Pichilemu | Días hábiles: $7000 | Sábado-Domingo: $8000")
        print("3) Santo Domingo | Días hábiles: $4000 | Sábado-Domingo: $5000")
        print(" ")
        print("Escriba el numero de la ubicación")
        print(" ")
        destino=int(input("Seleccione:  "))
        
        if destino==1:
            print(" ")
            destino="Valparaiso | 120KM"
            print(f"Usted eligió: {destino}")
            viajes+=[destino]
            dia=input("Qué día le gustaría viajar?:  ")
            
            if dia=="Lunes" or "Martes" or "Miercoles" or "Jueves" or "Viernes" or "lunes" or "martes" or "miercoles" or "jueves" or "viernes":
                print(" ")
                costo=5000
                print(f"El precio del día {dia} es de ${costo}")
                print(" ")
                print("Ingrese a la hora que quiere viajar")
                while True:
                    print("Utilice formato 24 hrs!")
                    try:
                        hora = int(input("Hora deseada:  "))
                    except ValueError:
                        print("Solo formato 24hrs!")
                    else:
                        print(f"Seleccionó las {hora} para viajar!")
                        break
                    
                if hora >= 13 and hora < 21:
                    print(" ")
                    print("Este es horario punta")
                    nuevoCosto=costo+(costo*0.30)
                    print(" ")
                    print(f"El nuevo costo será de ${nuevoCosto}")
                    print(" ")
                    print("Volverá al menú")
                else:
                    print(" ")
                    print("Seleccionó un horario normal")
                    nuevoCosto=5000
                    print(f"El costo será de ${nuevoCosto}")
                    print(" ")
                    print("Volverá al menú") 
            elif dia=="sabado" or "Sabado" or "sábado" or "Sábado" or "Domingo" or "domingo":
                costo=6000
                print(" ")
                print(f"El precio del día {dia} es de ${costo}")
                print(" ")
                print("Ingrese a la hora que quiere viajar")
                while True:
                    print("Utilice formato 24 hrs!")
                    try:
                        hora = int(input("Hora deseada:  "))
                    except ValueError:
                        print("Solo formato 24hrs!")
                    else:
                        print(f"Seleccionó las {hora} para viajar!")
                        break
                    
                if hora >= 13 and hora < 21:
                    print(" ")
                    print("Este es horario punta")
                    nuevoCosto=costo+(costo*0.30)
                    print(" ")
                    print(f"El nuevo costo será de ${nuevoCosto}")
                    print(" ")
                    print("Volverá al menú")
                else:
                    print(" ")
                    print("Seleccionó un horario normal")
                    nuevoCosto=6000
                    print(f"El costo será de ${nuevoCosto}")
                    print(" ")
                    print("Volverá al menú") 
            else:
                print("ERROR")
        elif destino==2:
            print(" ")
            destino="Pichilemu | 206KM"
            print(f"Usted eligió: {destino}")
            viajes+=[destino]
            dia=input("Qué día le gustaría viajar?:  ")
            
            if dia=="Lunes" or "Martes" or "Miercoles" or "Jueves" or "Viernes" or "lunes" or "martes" or "miercoles" or "jueves" or "viernes":
                print(" ")
                costo=7000
                print(f"El precio del día {dia} es de ${costo}")
                print(" ")
                print("Ingrese a la hora que quiere viajar")
                while True:
                    print("Utilice formato 24 hrs!")
                    try:
                        hora = int(input("Hora deseada:  "))
                    except ValueError:
                        print("Solo formato 24hrs!")
                    else:
                        print(f"Seleccionó las {hora} para viajar!")
                        break
                    
                if hora >= 13 and hora < 21:
                    print(" ")
                    print("Este es horario punta")
                    nuevoCosto=costo+(costo*0.30)
                    print(" ")
                    print(f"El nuevo costo será de ${nuevoCosto}")
                    print(" ")
                    print("Volverá al menú")
                else:
                    print(" ")
                    print("Seleccionó un horario normal")
                    nuevoCosto=7000
                    print(f"El costo será de ${nuevoCosto}")
                    print(" ")
                    print("Volverá al menú") 
            elif dia=="sabado" or "Sabado" or "sábado" or "Sábado" or "Domingo" or "domingo":
                print(" ")
                costo=8000
                print(f"El precio del día {dia} es de ${costo}")
                print(" ")
                print("Ingrese a la hora que quiere viajar")
                while True:
                    print("Utilice formato 24 hrs!")
                    try:
                        hora = int(input("Hora deseada:  "))
                    except ValueError:
                        print("Solo formato 24hrs!")
                    else:
                        print(f"Seleccionó las {hora} para viajar!")
                        break
                    
                if hora >= 13 and hora < 21:
                    print(" ")
                    print("Este es horario punta")
                    nuevoCosto=costo+(costo*0.30)
                    print(" ")
                    print(f"El nuevo costo será de ${nuevoCosto}")
                    print(" ")
                    print("Volverá al menú")
                else:
                    print(" ")
                    print("Seleccionó un horario normal")
                    nuevoCosto=8000
                    print(f"El costo será de ${nuevoCosto}")
                    print(" ")
                    print("Volverá al menú") 
            else:
                print("ERROR")
        elif destino==3:
            print(" ")
            destino="Santo Domingo | 144KM"
            print(f"Usted eligió: {destino}")
            viajes+=[destino]
            dia=input("Qué día le gustaría viajar?:  ")
            
            if dia=="Lunes" or "Martes" or "Miercoles" or "Jueves" or "Viernes" or "lunes" or "martes" or "miercoles" or "jueves" or "viernes":
                print(" ")
                costo=4000
                print(f"El precio del día {dia} es de ${costo}")
                print(" ")
                print("Ingrese a la hora que quiere viajar")
                while True:
                    print("Utilice formato 24 hrs!")
                    try:
                        hora = int(input("Hora deseada:  "))
                    except ValueError:
                        print("Solo formato 24hrs!")
                    else:
                        print(f"Seleccionó las {hora} para viajar!")
                        break
                    
                if hora >= 13 and hora < 21:
                    print(" ")
                    print("Este es horario punta")
                    nuevoCosto=costo+(costo*0.30)
                    print(" ")
                    print(f"El nuevo costo será de ${nuevoCosto}")
                    print(" ")
                    print("Volverá al menú")
                else:
                    print(" ")
                    print("Seleccionó un horario normal")
                    nuevoCosto=4000
                    print(f"El costo será de ${nuevoCosto}")
                    print(" ")
                    print("Volverá al menú") 
            elif dia=="sabado" or "Sabado" or "sábado" or "Sábado" or "Domingo" or "domingo":
                print(" ")
                costo=8000
                print(f"El precio del día {dia} es de ${costo}")
                print(" ")
                print("Ingrese a la hora que quiere viajar")
                while True:
                    print("Utilice formato 24 hrs!")
                    try:
                        hora = int(input("Hora deseada:  "))
                    except ValueError:
                        print("Solo formato 24hrs!")
                    else:
                        print(f"Seleccionó las {hora} para viajar!")
                        break
                    
                if hora >= 13 and hora < 21:
                    print(" ")
                    print("Este es horario punta")
                    nuevoCosto=costo+(costo*0.30)
                    print(" ")
                    print(f"El nuevo costo será de ${nuevoCosto}")
                    print(" ")
                    print("Volverá al menú")
                else:
                    print(" ")
                    print("Seleccionó un horario normal")
                    nuevoCosto=5000
                    print(f"El costo será de ${nuevoCosto}")
                    print(" ")
                    print("Volverá al menú") 
            else:
                print("ERROR")
        else:
            print("NO VÁLIDO")
    elif opc==2:
        print(" ")
        print("Estos son los datos que tenemos:")
        print(usuario)
        print(nuevoCosto)
        print(dia)
        print(hora)
        print(destino)
        print(" ")
        print("Desea confirmar la venta del pasaje? (SI/NO)")
        ventPas=input("Responda:  ")
        if ventPas=="SI" or "si" or "Si":
            print(f"El total a pagar es ${nuevoCosto}")
            while True:
                print("Por favor, proceda al pago")
                try:
                    pago1 = int(input("$:  ")) 
                except ValueError:
                    print("Por favor, solo ingrese números!")
                else:
                    print(f"Ingresó {pago1}$")
                    if pago1 > nuevoCosto:
                        print(f"Pago realizado! su vuelto es de {pago1-nuevoCosto}$")
                        print("Gracias por su preferencia!")
                        break
                    elif nuevoCosto > pago1:
                        print("No cuenta con el monto necesario, intentelo de nuevo")
                    else:
                        print("Pago realizado! Gracias por su preferencia")
                        break
        elif ventPas=="NO" or "no" or "No":
            print(" ")
            print("Volverá al menú principal")
    elif opc==3:
        print(" ")
        print("Cantidad de pedidos realizados:", len(viajes))
        print(" ")
        print("Pedidos realizados: ")
        for destino in viajes:
            print(destino, f"- {nuevoCosto}")
        break
    elif opc==4:
        print("Finalizando programa. Ha sido un gusto!")
        break