from claseNodo import nodo

class colaE:
    __cant: int
    __prim: nodo
    __ulti: nodo

    def __init__(self):
        self.__cant = 0
        self.__prim = None
        self.__ulti = None

    def vacia(self):
        return self.__cant == 0

    def insertar(self, x):
        nodoNuevo = nodo(x)
        nodoNuevo.setSiguiente(None)
        if (self.__ulti is None):
            self.__prim = nodoNuevo
        else:
            self.__ulti.setSiguiente(nodoNuevo)
        self.__ulti = nodoNuevo
        self.__cant += 1
        return x
    
    def suprimir(self):
        if (self.vacia()):
            raise Exception("Cola vacia")
        else:
            x = self.__prim.getObjeto()
            self.__prim = self.__prim.getSiguiente()
            self.__cant -= 1
            return x
    
    def recuperar(self):
        if (self.vacia()):
            raise Exception("Cola vacia")
        else:
            x = self.__prim.getObjeto()
            return x

    