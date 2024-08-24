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
            return elemento 

    def __iter__(self):
        return self

    def __next__(self):
        if self.__tope == -1:
            raise StopIteration
        else:
            elemento = self.__lista[self.__tope]
            self.__tope -= 1
            return elemento
