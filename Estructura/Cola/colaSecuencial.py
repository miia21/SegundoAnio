import numpy as np

class colaS:
    __item: np.ndarray
    __prim: int
    __ulti: int
    __max: int
    __cant: int

    def __init__(self):
        self.__item = np.empty(10, dtype=int)
        self.__max = 10
        self.__cant = 0
        self.__prim = 0
        self.__ulti = -1

    def vacia(self):
        return self.__cant == 0
    
    def lleno(self):
        return self.__max == self.__cant
    
    def insertar(self, x):
        if (self.lleno()):
            raise Exception("Cola llena")
        else:
            self.__item[self.__ulti] = x
            self.__ulti = (self.__ulti + 1) % self.__max
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