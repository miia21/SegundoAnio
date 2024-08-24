from gestorAlquiler import gestorAlquiler
from gestorCancha import gestorCancha

def menu():
    print("Menu\n 1-Listar alquiler\n 2-Buscar cancha\n 3-Salir\n")

if __name__=='__main__':
    alquiler=gestorAlquiler()
    alquiler.carga()
    cancha=gestorCancha()
    cancha.cargar()
    menu()
    o=int(input("Ingrese una opcion\n"))
    while(o!=3):
        if(o==1):
            alquiler.listado(cancha)
        elif(o==2):
            alquiler.cancha()
        else:
            print(f"La opcion ingresada es incorrecta")
        menu()
        o=int(input("Ingrese una opcion\n"))