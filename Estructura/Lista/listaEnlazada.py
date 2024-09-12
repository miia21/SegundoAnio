from claseNodo import nodo

class listaE:
    __cabeza: nodo
    __cant: int

    def __init__(self):
        self.__cabeza = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0
    
    def insertarPosicion(self, x, p):
        p=p-1
        nuevoNodo = nodo(x)
        if (self.vacia()):
            self.__cabeza = nuevoNodo
            self.__cant += 1
        else:
            if (p == 0):
                nuevoNodo.setSiguiente(self.__cabeza)
                self.__cabeza = nuevoNodo
                self.__cant += 1
            elif (p <= self.__cant):
                i=0
                actual = self.__cabeza
                while i<p-1:
                    actual = actual.getSiguiente()
                    i+=1
                nuevoNodo.setSiguiente(actual.getSiguiente())
                actual.setSiguiente(nuevoNodo)
                self.__cant += 1
            else:
                raise Exception("Posicion fuera de rango")
        return x
    
    def suprimir(self, p):
        p=p-1
        if self.__cant == 0:
            raise Exception("Lista vacia")
        elif p == 0:
            elemento = self.__cabeza
            self.__cabeza = self.__cabeza.getSiguiente()
            self.__cant -= 1
        elif p <= self.__cant:
            i=0
            actual = self.__cabeza
            while i<p-1:
                anterior = actual
                actual = actual.getSiguiente()
                i+=1
            anterior.setSiguiente(actual.getSiguiente())
            self.__cant -= 1
        else:
            raise Exception("Posicion fuera de rango")
        
    def recuperar(self, p):
        p=p-1
        if self.__cant == 0:
            raise Exception("Lista vacia")
        else:
            actual = self.__cabeza
            i = 0
            while i < p-1:
                actual = actual.getSiguiente()
                i += 1
            return actual.getObjeto()
        
    def buscar(self, x):
        if self.__cant == 0:
            raise Exception("Lista vacia")
        else:
            i = 0
            actual = self.__cabeza
            while actual.getObjeto() != x:
                actual = actual.getSiguiente()
                i += 1
            if i == self.__cant:
                raise Exception("Elemento no encontrado")
            else:
                return i
            
    def primerElemento(self):
        if self.__cant == 0:
            raise Exception("Lista vacia")
        else:
            return self.__cabeza.getObjeto()
        
    def ultimoElemento(self):
        if self.__cant == 0:
            raise Exception("Lista vacia")
        else:
            actual = self.__cabeza
            while actual is not None:
                actual = actual.getSiguiente()
                i += 1
            return actual.getObjeto()
        
    def anterior(self, p):
        p=p-1
        if p<=0 or p>self.__cant:
            raise Exception("Posicion fuera de rango")
        else:
            return p-1
    
    def siguiente(self, p):
        p=p-1
        if p<0 or p>=self.__cant:
            raise Exception("Posicion fuera de rango")
        else:
            return p+1
        
    def mostrar(self):
        if self.__cant == 0:
            raise Exception("Lista vacia")
        else:
            actual = self.__cabeza
            while actual is not None:
                print(actual.getObjeto())
                actual = actual.getSiguiente()