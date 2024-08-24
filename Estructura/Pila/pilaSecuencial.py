import numpy as np

class pilaS:
    __item: np.ndarray
    __tope: int
    __cant: int

    def __init__(self):
        self.__item = np.empty(10, dtype=int)
        self.__tope = -1
        self.__cant = 10

    def vacia(self):
        return self.__tope == -1
    
    def lleno(self):
        return self.__tope == self.__cant - 1
    
    def insertar(self, x):
        if (self.__tope == self.__cant - 1):
            raise Exception("Pila llena")
        else:
            self.__tope += 1
            self.__item[self.__tope] = x
            return x

    def suprimir(self):
        if (self.vacia()):
            raise Exception("Pila vacia")
        else:
            x = self.__item[self.__tope]
            self.__tope -= 1
            return x
        
    def mostrar(self):
        if (self.vacia()):
            raise Exception("Pila vacia")
        else:
            for i in range(self.__tope, -1, -1):
                print(self.__item[i], end=" ")