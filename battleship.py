#jogo


import random
tablero=[
    ["-","-","-","-","-"],
    ["-","-","-","-","-"],
    ["-","-","-","-","-"],
    ["-","-","-","-","-"],
    ["-","-","-","-","-"],
]

FilaBarcos=[]
ColumnBarcos=[]
municion=10


for i in range(3):
    FilaPosi=random.randint(0,4)
    ColPosi=random.randint(0,4)
    FilaBarcos.append(FilaPosi)
    ColumnBarcos.append(ColPosi)
    #tablero[FilaPosi][ColPosi]="B"
    barcosEliminados=0
    
    
print("Bienvenido jugador.\n Estás a punto de comenzar la batalla, ¿Estás preparado?:  ")
resp=input("> ").lower()


if resp=="si":
    print(FilaBarcos)
    print(ColumnBarcos)
    for fila in tablero:
        print(fila)

    print(" ")
    print("Hay 3 barcos en el mapa repartidos aleatoreamente. Debes hundirlo indicando las coordenadas donde crees que se encuentran")
    print(" ")
    print("Las coordenadas deben corresponder a una matiz de 5x5. Por ejemplo, fila 1 y columna 3")
    while True:
        print(" ")
        fila=int(input("Ingrese la fila en la que cree que se encuentra el barco:  "))
        columna=int(input("Ingrese la columna en la que cree que se encuentra el barco:  "))
        if fila > 5 or columna > 5 or fila<=0 or columna<=0:
            print(" ")
            print("Los valores no pueden ser mayores a 5, ni menores a 1")
            continue
        else:
            try:
                municion-=1
                fila-=1
                columna-=1
                FilaBarcos.index(fila)
                ColumnBarcos.index(columna)
                print("Tu disparo se pierde en la distancia")
            except ValueError:
                print("No le has dado")
                tablero[fila][columna]="0"    
            else:
                if tablero[fila][columna]=="X":
                    print("Ese barco se encuentra destruido")
                else:
                    print("Le has dado!")
                    tablero[fila][columna]="X"
                    barcosEliminados+=1
                
        
        for fila in tablero:
            print(fila)
        
        print(f"Munición restante: {municion}")
        
        if barcosEliminados==len(ColumnBarcos):
            print(" ")
            print("Has eliminado a todos los barcos. Felicidades!")
            print(" ")
            print(f"Barcos hundidos: {barcosEliminados}")
            break
        elif municion==0:
            print(" ")
            print("Te has quedado sin munición")
            print(" ")
            print(f"Barcos hundidos:{barcosEliminados}")
            print(" ")
            print("Suerte en tu próxima partida!")
            
            for fila in FilaBarcos:
                for col in ColumnBarcos:
                    if tablero[fila][columna]!="X":
                        tablero[fila][columna]="B"
            
            break
    
else:
    print("Hasta pronto")    
