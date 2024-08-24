from gestorCab import gestorCabana
from gestorRes import gestorReserva

def menu():
    print("Menu\n 1-Buscar cabaña\n 2-Buscar fecha\n 3-Salir\n")

if __name__=='__main__':
    cabanas=gestorCabana()
    cabanas.cargar()
    reservas=gestorReserva()
    reservas.cargar()
    menu()
    o=int(input("Ingrese una opcion\n"))
    while(o!=3):
        if(o==1):
            cabanas.burcarcab(reservas)
        elif(o==2):
            reservas.fechas(cabanas)
        else:
            print(f"La opcion ingresada es incorrecta")
        menu()
        o=int(input("Ingrese una opcion\n"))
    