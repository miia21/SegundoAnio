from gestorVenta import gestor

if __name__ == '__main__':
    arreglo=gestor()
    print("Menu\n 1- Cargar datos\n 2- Mostrar datos\n 3- Ver facturacion semanal de una sucursal\n 4- Ver sucursal que mas facturó\n 5- Ver sucursal que menos facturó en la semana\n 6- Ver total facturado\n 7- Salir\n")
    o = int(input("Ingrese una opcion\n"))
    while(o!=7):
        if(o==1):
            arreglo.cargaDatos()
        elif(o==2):
            arreglo.mostrarArreglo()
        elif(o==3):
            arreglo.facSucursal()
        elif(o==4):
            arreglo.facDia()
        elif(o==5):
            arreglo.menosFac()
        elif(o==6):
            arreglo.facTotal()
        else:
            print(f"La opcion ingresada es incorrecta")
        print("Menu\n 1- Cargar datos\n 2- Mostrar datos\n 3- Ver facturacion semanal de una sucursal\n 4- Ver sucursal que mas facturó\n 5- Ver sucursal que menos facturó en la semana\n 6- Ver total facturado\n 7- Salir\n")
        o=int(input("Ingrese una opcion\n"))
    
    