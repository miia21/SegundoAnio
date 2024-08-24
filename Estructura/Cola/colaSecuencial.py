import numpy as np

class colaS:
    __item: np.ndarray
    __prim: int
    __ulti: int
    __tope: int
    __cant: int

    def __init__(self):
        self.__item = np.empty(10, dtype=int)
        self.__tope = 0
        self.__cant = 10
        self.__prim = 0
        self.__ulti = -1

    def vacia(self):
        return self.__cant == 0
    
    def lleno(self):
        return self.__tope == self.__cant
    
    def insertar(self, x):
        if (self.__tope == self.__cant):
            raise Exception("Cola llena")
        else:
            self.__item[self.__ulti] = x
            self.__ulti = (self.__ulti + 1) % self.__tope
            self.__cant += 1
            return x
        
    def suprimir(self):
        if (self.vacia()):
            raise Exception("Cola vacia")
        else:
            x = self.__item[self.__prim]
            self.__prim = (self.__prim + 1) % self.__tope
            self.__cant -= 1
            return x
    
    def mostrar(self):
        if (self.vacia()):
            raise Exception("Cola vacia")
        else:
            for i in range(self.__prim, self.__ulti):
                print(self.__item[i], end=" ")