from claseNodo import nodo
import numpy as np

class listaC:
    __max: int
    __cabeza: int
    __cant: int
    __disp: int
    __espacio: np.ndarray

    def __init__(self, xmax=10):
        self.__max = xmax
        self.__cabeza = 0
        self.__cant = 0
        self.__disp = 0
        self.__espacio = np.empty(xmax, dtype=nodo)
        i=0
        for i in range(max):
            
    def vacia(self):
        return self.__cant == 0
    
    def getDisp(self):
        i=0
        while i<self.__max and self.__espacio[i].getSiguiente() != None:
            i+=1
        if  i<self.__max:
            self.__disp = i
            return True
        else:
            self.__disp = None
            return False
        
    