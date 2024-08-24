from claseLista import lista

def menu():
    print("Menu\n1- Agregar elemento\n2- Mostrar tipo\n3- Mostrar cantidad\n4- Mostrar todo\n5- salir")

if __name__ == "__main__":
    lista=lista()
    lista.carga()
    menu()
    o=int(input("Ingrese una opcion\n"))
    while(o!=5):
        if(o==1):
            lista.agregar()
        elif(o==2):
            lista.cantPos()
        elif(o==3):
            lista.cantidad()
        elif(o==4):
            lista.mostrar()
        else:
            print(f"La opcion ingresada es incorrecta")
        menu()
        o=int(input("Ingrese una opcion\n"))