from claseLista import lista

def menu():
    print("Menu\n1- Agregar elemento\n2- Mostrar servicios de transporte\n3- Cantidad de servicios de embalaje\n4- fecha\n5- salir")

if __name__=='__main__':
    lista=lista()
    lista.carga()
    menu()
    o=int(input("Ingrese una opcion\n"))
    while(o!=5):
        if(o==1):
            lista.agregar()
        elif(o==2):
            lista.mostrar()
        elif(o==3):
            lista.cantidad()
        elif(o==4):
            lista.fecha()
        else:
            print(f"La opcion ingresada es incorrecta")
        menu()
        o=int(input("Ingrese una opcion\n"))