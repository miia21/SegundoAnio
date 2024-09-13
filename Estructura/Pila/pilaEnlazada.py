from claseNodo import nodo

class pilaE:
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
        self.__tope = nuevoNodo
        self.__cant += 1
        return nuevoNodo.getObjeto()

    def suprimir(self):
        if (self.vacia()):
            print("Pila vacia")
        else:
            x = self.__tope.getObjeto()
            self.__tope = self.__tope.getSiguiente()
            self.__cant -= 1
            return x
        
    def mostrar(self):
        actual = self.__tope
        while actual is not None:
            print(actual.getObjeto(), end=" ")
            actual = actual.getSiguiente()
        print()