#nombresyapellidos

nombres=[]
apellidos=[]

print("Por favor, escriba 3 nombres y 3 apellidos")

for i in range(3):
    nombre=input("Escriba nombres:  ")
    nombres.append(nombre)
    
for i in range(3):
    apellido=input("Escriba apellidos:  ")
    apellidos.append(apellido)
   
print("Estos son los nombres y apellidos:  ")   
for i in range (3):
    
    print(f"{nombres[i]} {apellidos[i]}")