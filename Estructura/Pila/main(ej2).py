from pilaSecuencial import pila

if __name__ == "__main__":
    p = pila()
    x=int(input("Ingrese un numero\n"))
    if x == 0:
        print("0 0 0 0\n")
    else:
        while x > 0:
            aux = x
            resto = x % 2
            p.insertar(resto)
            x = x // 2
        while not p.vacia():
            print(p.suprimir(), end=" ")