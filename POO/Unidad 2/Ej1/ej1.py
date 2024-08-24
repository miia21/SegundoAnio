from claseCajaAhorro import cajaAhorro

def test():
    num=int(input("Ingrese el numero de cuenta\n"))
    cuil=input("Ingrese el cuil\n")
    ap=input("Ingrese el apellido\n")
    nom=input("Ingrese el nombre\n")
    sal=float(input("Ingrese el saldo\n"))
    caja=cajaAhorro(num, cuil, ap, nom, sal)
    if(caja.validarCuil()==False):
        print(f"El cuil ingresado es incorrecto")
    else:
        print("Menu\n 1- Mostrar datos\n 2- Extaer\n 3- Depositar\n 4- Salir\n")
        o = int(input("Ingrese una opcion\n"))
        while(o!=4):
            if(o==1):
                caja.mostrarDatos()
            elif(o==2):
                imp=float(input("Ingrese el monto a retirar\n"))
                caja.extraer(imp)
            elif(o==3):
                imp=float(input("Ingrese el monto a ingresar\n"))
                caja.depositar(imp)
            else:
                print(f"La opcion ingresada es incorrecta")
            o=int(input("Ingrese una opcion\n"))

if __name__ == '__main__':
    test()
    test()
    test()
    
    


    