from ClasePila import Pila

if __name__ == "__main__":
    pila = Pila()
    elemento = int(input("Ingrese un numero decimal: "))
    if elemento == 0:
        print("0 0 0 0")
    else:
        while elemento > 0:
            aux = elemento
            resto = elemento % 2
            pila.insertar(resto)
            elemento = elemento // 2
        while not pila.Vacio():
            print(pila.Suprimir(), end=" ")
        
        