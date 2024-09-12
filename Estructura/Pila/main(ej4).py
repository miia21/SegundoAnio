from pilaEnlazada import pilaE

if __name__ == "__main__":
    torre1 = pilaE()
    torre2 = pilaE()
    torre3 = pilaE()
    torre1.insertar(4)
    torre1.insertar(3)
    torre1.insertar(2)
    torre1.insertar(1)
    torres = [torre1, torre2, torre3]
    print("Las torres son:")
    for i in range(3):
        print(f"Torre {i+1}", end=": ")
        elementos = torres[i].mostrar()
        print()
    while torre3.vacia() or not torre2.vacia() or not torre1.vacia():
        sacar = int(input("Escriba la torre de la que desea sacar un disco:\n"))
        try:
            disco = torres[sacar-1].suprimir()
            colocar = int(input("Escriba la torre en la que desea poner un disco:\n"))
            disco2 = torres[colocar-1].suprimir()
            if disco2 is None:
                torres[colocar-1].insertar(disco)
            elif disco2 > disco:
                torres[colocar-1].insertar(disco2)
                torres[colocar-1].insertar(disco)
            else:
                print("El disco no puede ser colocado en la torre porque es mayor que el que hay en ella\n")
                torres[sacar-1].insertar(disco)
                torres[colocar-1].insertar(disco2)
        except IndexError:
            print("Torre inválida seleccionada.\n")
            continue
        print("Las torres son:")
        for i in range(3):
            print(f"Torre {i+1}", end=": ")
            elementos = torres[i].mostrar()
            print()
    print("Ganaste")