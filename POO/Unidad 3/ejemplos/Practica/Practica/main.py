from gestorPlanes import Lista

def menu():
    print("Menu\n1- Mostrar por posicion\n2- Mostrar cantidad por cobertura\n3- Mostrar cantidad de canales\n4- Mostrar todo\n5- Salir")

if __name__=='__main__':
    lista1=Lista()
    lista1.carga()
    menu()
    o=int(input("Ingrese una opcion\n"))
    while(o!=5):
        if(o==1):
            try:
                lista1.pos()
            except IndexError:
                print("Indice fuera de rango\n")
        elif(o==2):
            lista1.contador()
        elif(o==3):
            lista1.canales()
        elif(o==4):
            lista1.mostrar()
        else:
            print(f"La opcion ingresada es incorrecta\n")
        menu()
        o=int(input("Ingrese una opcion\n"))