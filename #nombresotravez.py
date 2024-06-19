#nombresotravez

nombres=[]

print("Por favor ingrese la cantidad de nombres que desee:  ")

while True:
    nombre=input("Nombre:  ")
    nombres.append(nombre)
    
    opc=input("Desea escribir más nombres? (SI/NO):  ").lower()
    if opc=="no":
        print("Entendido")
        break
        
    elif opc=="si":
        print("Siga entonces")
        print(" ")
        
nombre_min=min(nombres, key=len)
print("El nombre más pequeño es: ", nombre_min)
print(" ")
print("Este se eliminará")