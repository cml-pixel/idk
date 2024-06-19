

nombres=[]


for i in range(3):
    nombre=input("Ingrese nombres:  ")
    nombres.append(nombre)
    
nombre_max=max(nombres, key=len)
print("El nombre más largo es: ", nombre_max)