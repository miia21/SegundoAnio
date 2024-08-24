from claseNodo import nodo

class pila:
    __cant: int
    __tope: nodo

    def __init__(self):
        self.__cant = 0
        self.__tope = None

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, x):
        nuevoNodo = nodo(x)
        nuevoNodo.setSiguiente(self.__tope)
        self.__tope = nodo
        self.__cant += 1
        return nuevoNodo.getObjeto()

    def suprimir(self):
        if (self.vacia()):
            raise Exception("Pila vacia")
        else:
            x = self.__tope.getObjeto()
            self.__tope = self.__tope.getSiguiente()
            self.__cant -= 1
            return x
        
    def mostrar(self):
        if (self.vacia()):
            raise Exception("Pila vacia")
        else:
            for i in range(self.__cant):
                print(self.__tope.getObjeto(), end=" ")
                self.__tope = self.__tope.getSiguiente()
            print()