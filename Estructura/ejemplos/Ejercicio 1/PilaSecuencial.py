import numpy as np
class Pila:
    __dimension: int   
    __tope: int
    __lista: np.ndarray
    def __init__(self):
        self.__lista = np.zeros(10, dtype=int)  
        self.__tope = -1
        self.__dimension = 10

    def lleno(self):
        return self.__tope == self.__dimension - 1

    def insertar(self, x):
        if not self.lleno():  
            self.__tope += 1
            self.__lista[self.__tope] = x
        else:
             print("Pila Llena")
             

    def Vacio(self):
        return self.__tope == -1

    def Suprimir(self):
        if self.Vacio():
            print("Error: Pila Vacia")
            return True
        else:
            elemento = self.__lista[self.__tope]
            self.__tope -= 1
            return elemento, self.__lista

    def __iter__(self):
        return self

    def __next__(self):
        if self.__tope == -1:
            raise StopIteration
        else:
            elemento = self.__lista[self.__tope]
            self.__tope -= 1
            return elemento



if __name__ == "__main__":
    pila = Pila()
    print(pila.Vacio())
    pila.insertar(1)
    pila.insertar(2)
    pila.insertar(3)
    pila.insertar(4)
    pila.insertar(5)
    print(pila.Vacio()) 
    print(pila.lleno())  
    
    elemento, lista_pila = pila.Suprimir()
    print(f"Elemento suprimido: {elemento}")
    print(f"Lista actual: {lista_pila}")
    print(pila.lleno())
    
    elemento, lista_pila = pila.Suprimir()
    print(f"Elemento suprimido: {elemento}")
    print(f"Lista actual: {lista_pila}")
    print(pila.lleno())

