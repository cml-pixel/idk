#menú


def eliminar_usuario(usuario, contraseña):
    if usuario in correos:
        index = correos.index(usuario)
        if contrasenias[index] == contraseña:
            del correos[index]
            del contrasenias[index]
            print("Usuario eliminado con éxito. Volverá al menú")
            print(" ")
            return
        else:
            print("El usuario no existe o la contraseña es incorrecta. Intentelo de nuevo")
            print(" ")


correos=[]
contrasenias=[]

print("Bienvenido! Qué desea hacer?")
print(" ")
while True:
    print("1) Crear usuario y contraseña")
    print(" ")
    print("2) Eliminar usuario")
    print(" ")
    print("3) Ver usuarios registrados")
    print(" ")
    print("4) Salir")
    print(" ")
    opc2=int(input("Seleccione:  "))

    if opc2==1:
        while True:
            corr=input("Por favor, cree un usuario:  ")
            correos.append(corr)
            print(" ")
            contr=input("Por favor, ingrese una contraseña:  ")
            contrasenias.append(contr)
            print(" ")
    
            opc=input("Desea seguir agragando usuarios? (SI/NO):  ").lower()
    
            if opc=="no":
                print("Entendido. Se dejará de agregar usuarios")
                print(" ")
                break
            elif opc=="si":
                print("Continue")
                print(" ")
            
    elif opc2==2:
        print(" ")
        user_del=input("Escriba el usuario que desea eliminar:  ")
        pass_del = input("Escriba la contraseña asociada al usuario que desea eliminar: ")
        print(" ")
        eliminar_usuario(user_del, pass_del)
    
    elif opc2==3:
        print(" ")
        print("Estos son los usuarios y contraseñas:  ")
        print(" ")
        for i in range(len(correos)):
            print(f"USUARIO: {correos[i]} CONTRASEÑA: {contrasenias[i]}")
            print(" ")
        
    elif opc2==4:
        print(" ")
        print("Saliendo, muchas gracias")
        break
    else:
        print("NO VÁLIDO")