import numpy as np

class Pila:
    __ul: int
    __cant: int
    __pri: int
    __max: int
    __lista: np.ndarray
    def __init__(self, ult=0, cant=0, pri=0,max=0):
        self.__ul = 0
        self.__cant = 0
        self.__pri = 0
        self.__max = max
        self.__lista = np.zeros(self.__max, dtype=int)
    def vacio(self):
        return self.__cant == 0
    def lleno(self):
        return self.__cant == self.__max
    def insertar(self,dato):
        if self.__cant < self.__max:
            self.__lista[self.__ul] = dato
            self.__ul = (self.__ul+1)%self.__max
            self.__cant += 1
            return dato
        else:
            return True
        
    def suprimir(self):
        if self.vacio():
            print("La pila esta vacia")
            return True
        else:
            aux = self.__lista[self.__pri]
            self.__pri = (self.__pri+1)%self.__max
            self.__cant -= 1
            return aux
    def recorrer(self):
        if self.vacio():
            print("La pila esta vacia")
            return True
        else:
            i = self.__pri
            for j in range(self.__cant):
                print(self.__lista[i])
                i = (i + 1) % self.__max


if __name__ == "__main__":
    pila = Pila(max=10)
    pila.insertar(1)
    pila.insertar(2)
    pila.insertar(3)
    pila.insertar(4)
    pila.insertar(5)
    pila.insertar(6)
    pila.insertar(7)
    pila.insertar(8)
    pila.insertar(9)
    pila.insertar(10)
    pila.recorrer()
    print("Surpime")
    print(pila.suprimir())
    print("Recorre")
    pila.recorrer()
    print("Surpime")
    print(pila.suprimir())