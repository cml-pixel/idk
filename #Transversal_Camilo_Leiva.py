#Transversal_Camilo_Leiva

import random
import csv

trabajadores = [
    {"nombre": "Juan Perez"},
    {"nombre": "Maria Garcia"},
    {"nombre": "Carlos Lopez"},
    {"nombre": "Ana Martinez"},
    {"nombre": "Pedro Rodriguez"},
    {"nombre": "Laura Hernandez"},
    {"nombre": "Miguel Sanchez"},
    {"nombre": "Isabel Gomez"},
    {"nombre": "Francisco Diaz"},
    {"nombre": "Elena Fernandez"}
]

def asignar_sueldos():
    for empleado in trabajadores:
        empleado['sueldo'] = random.randint(300000, 2500000)

def clasificar_sueldos():
    sueldos_menor_800k = []
    sueldos_entre_800k_2m = []
    sueldos_mayor_2m = []
    
    for empleado in trabajadores:
        if empleado['sueldo'] < 800000:
            sueldos_menor_800k.append(empleado)
        elif 800000 <= empleado['sueldo'] <= 2000000:
            sueldos_entre_800k_2m.append(empleado)
        else:
            sueldos_mayor_2m.append(empleado)
    
    print("-"*32)
    print(f"Sueldos menores a $800000 TOTAL: {len(sueldos_menor_800k)}\n")
    for emp in sueldos_menor_800k:
        print(f"Nombre empleado:  {emp['nombre']:20} ${emp['sueldo']}")
    print("-"*32)
    print(f"\nSueldos entre $800000 y $2000000 TOTAL: {len(sueldos_entre_800k_2m)}\n")
    for emp in sueldos_entre_800k_2m:
        print(f"Nombre empleado:  {emp['nombre']:20} ${emp['sueldo']}")
    print("-"*32)
    print(f"\nSueldos superiores a $2000000 TOTAL: {len(sueldos_mayor_2m)}\n")
    for emp in sueldos_mayor_2m:
        print(f"Nombre empleado:  {emp['nombre']:20} ${emp['sueldo']}")
    print("-"*32)
    total_sueldos = sum(emp['sueldo'] for emp in trabajadores)
    print(f"\nTOTAL SUELDOS: ${total_sueldos}\n")
    print("-"*32)

def ver_estadisticas():
    sueldos = [emp['sueldo'] for emp in trabajadores]
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(trabajadores)
    
    #mediaGeometricaRaraXD
    producto_sueldos = 1
    for sueldo in sueldos:
        producto_sueldos *= sueldo
    media_geometrica = producto_sueldos ** (1 / len(trabajadores))
    
    print("-"*35)
    print(f"Sueldo más alto: ${sueldo_maximo}")
    print(f"Sueldo más bajo: ${sueldo_minimo}")
    print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
    print(f"Media geométrica de sueldos: ${media_geometrica:.2f}")
    print("-"*35)
def generar_reporte():
    with open('reporte_sueldos.csv', 'w', newline='') as csvfile:
        fieldnames = ['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Liquido']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for emp in trabajadores:
            descuento_salud = emp['sueldo'] * 0.07
            descuento_afp = emp['sueldo'] * 0.12
            sueldo_liquido = emp['sueldo'] - descuento_salud - descuento_afp
            
            writer.writerow({
                'Nombre empleado': emp['nombre'],
                'Sueldo Base': f"${emp['sueldo']}",
                'Descuento Salud': f"${descuento_salud:.2f}",
                'Descuento AFP': f"${descuento_afp:.2f}",
                'Sueldo Liquido': f"${sueldo_liquido:.2f}"
            })
    
    print("Reporte generado correctamente en 'reporte_sueldos.csv'")

def main():
    asignar_sueldos()
    
    while True:
        print("\n--- MENÚ ---")
        print("1) Asignar sueldos aleatorios")
        print("2) Clasificar sueldos")
        print("3) Ver estadísticas")
        print("4) Generar reporte de sueldos")
        print("5) Salir del programa")

        opcion = input("\nSeleccione una opción: ")
        print(" ")
        
        if opcion == '1':
            asignar_sueldos()
            print("Sueldos aleatorizados!")
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            generar_reporte()
        elif opcion == '5':
            print("\nFinalizando programa...")
            print(" ")
            print(input("Desarrollado por: "))
            print(" ")
            print(input("RUT: "))
            print(" ")
            print("Gracias!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida")
    
if __name__ == "__main__":
    main()