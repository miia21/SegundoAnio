from Pila import Pila

if __name__ == "__main__":
    pila = Pila()
    factorial = 1
    elemento = int(input("Ingrese un numero: "))
    if elemento == 0:
        print("El factorial de 0 es 1")
    else:
        numero = elemento
        while elemento > 0:
            pila.insertar(elemento)
            elemento -= 1
        while pila.Vacio() == False:
            factorial *= pila.Suprimir()
        print("El factorial de", numero, "es", factorial)