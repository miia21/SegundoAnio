import numpy as np

class listaS:
    __items: np.ndarray
    __cant: int
    __ulti: int

    def __init__(self):
        self.__items = np.empty(10, dtype=int)
        self.__cant = 0
        self.__ulti = -1
    
    def vacia(self):
        return self.__cant == 0
    
    def lleno(self):
        return self.__ulti == self.__cant
    
    def insertarPosicion(self, x, p):
        p=p-1
        if (self.lleno()):
            raise Exception("Lista llena")
        else:
            if (p < 0 or p > self.__ulti):
                raise Exception("Posicion invalida")
            elif (p == self.__ulti+1):
                self.__items[p] = x
                self.__ulti += 1
                self.__cant += 1
            else:
                for i in range(self.__ulti, p - 1, -1):
                    self.__items[i + 1] = self.__items[i]
                self.__items[p] = x
                self.__ulti += 1
                self.__cant += 1
            return x
        
    def suprimirPosicion(self, p):
        p=p-1
        if (self.vacia()):
            raise Exception("Lista vacia")
        else:
            if (p < 0 or p > self.__ulti):
                raise Exception("Posicion invalida")
            elif (p == self.__ulti):
                x = self.__items[p]
                self.__ulti -= 1
                self.__cant -= 1
            else:
                x = self.__items[p]
                for i in range(p, self.__ulti - 1):
                    self.__items[i] = self.__items[i + 1]
                self.__ulti -= 1
                self.__cant -= 1
            return x
        
    def recuperar(self, p):
        p=p-1
        if (self.vacia()):
            raise Exception("Lista vacia")
        else:
            if (p < 0 or p > self.__ulti):
                raise Exception("Posicion invalida")
            else:
                return self.__items[p]
            
    def buscar(self, x):
        if (self.vacia()):
            raise Exception("Lista vacia")
        else:
            i=0
            while (i <= self.__ulti):
                if (self.__items[i] == x):
                    return i
                else:
                    i += 1
            raise Exception("Elemento no encontrado")

    def primerElemento(self):
        if (self.vacia()):
            raise Exception("Lista vacia")
        else:
            return self.__items[0]
    
    def ultimoElemento(self):
        if (self.vacia()):
            raise Exception("Lista vacia")
        else:
            return self.__items[self.__ulti]
        
    def mostrar(self):
        if (self.vacia()):
            raise Exception("Lista vacia")
        else:
            for i in range(self.__ulti):
                print(f"{self.__items[i]}\n")

        
    