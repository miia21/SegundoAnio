from gestorCliente import gestorCliente
from gestorMovimiento import gestorMovimiento

if __name__ == '__main__':
    clientes=gestorCliente()
    clientes.cargar()
    movimientos=gestorMovimiento()
    movimientos.cargar()
    print("Menu\n 1- Actualizar saldo\n 2- Mostrar clientes sin movimientos\n 3- Ordenar movimientos\n 4- Salir\n")
    o=int(input("Ingrese una opcion\n"))
    while(o!=4):
        if(o==1):
            clientes.actualizar(movimientos)
        elif(o==2):
            clientes.movimientos(movimientos)
        elif(o==3):
            movimientos.ordenar()
        else:
            print(f"La opcion ingresada es incorrecta")
        print("Menu\n 1- Actualizar saldo\n 2- Mostrar clientes sin movimientos\n 3- Ordenar movimientos\n 4- Salir\n")
        o=int(input("Ingrese una opcion\n"))
