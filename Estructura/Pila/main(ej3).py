from pilaSecuencial import pila

if __name__ == "__main__":
    p = pila()
    fac=1
    x=int(input("Ingrese un numero\n"))
    if x == 0:
        print("El factorial es 1\n")
    while x > 0:
        p.insertar(x)
        x-=1
    while not p.vacia():
        fac*=p.suprimir()
    print(f"El factorial es {fac}")
    