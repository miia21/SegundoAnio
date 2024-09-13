import numpy as np

class listaS:
    __items: np.ndarray
    __ul: int

    def __init__(self):
        self.__items = np.empty(10, dtype=int)
        self.__ul = -1
    
    def vacia(self):
        return self.__ul == -1
    
    def lleno(self):
        return self.__ul == len(self.__items)-1
    
    def insertar(self, x):
        if self.lleno():
            raise Exception("Lista llena")
        else:
            pos = 0
            while pos <= self.__ul and self.__items[pos] < x:
                pos += 1
            for i in range(self.__ul, pos-1, -1):
                self.__items[i+1] = self.__items[i]
            self.__items[pos] = x
            self.__ul += 1
    
    def suprimirPosicion(self, p):
        if self.vacia():
            raise Exception("Lista vacía")
        elif p < 0 or p > self.__ul:
            raise Exception("Posición inválida")
        else:
            x = self.__items[p]
            for i in range(p, self.__ul):
                self.__items[i] = self.__items[i + 1]
            self.__ul -= 1
            return x

    def recuperar(self, p):
        if self.vacia():
            raise Exception("Lista vacía")
        elif p < 0 or p > self.__ul:
            raise Exception("Posición inválida")
        else:
            return self.__items[p]
            
    def buscar(self, x):
        if self.vacia():
            raise Exception("Lista vacía")
        else:
            piso = 0
            techo = self.__ul
            medio = int((piso + techo) / 2)
            while piso <= techo and self.__items[medio] != x:
                if self.__items[medio] < x:
                    piso = medio +1
                else:
                    techo = medio -1
                medio = int((piso + techo) / 2)
            if self.__items[medio] == x:
                indice = medio
            else:
                indice = -1
            return indice

    def primerElemento(self):
        if self.vacia():
            raise Exception("Lista vacía")
        else:
            return self.__items[0]
    
    def ultimoElemento(self):
        if self.vacia():
            raise Exception("Lista vacía")
        else:
            return self.__items[self.__ul]
        
    def mostrar(self):
        if self.vacia():
            raise Exception("Lista vacía")
        else:
            for i in range(self.__ul+1):
                print(self.__items[i], end=" ")
            print()