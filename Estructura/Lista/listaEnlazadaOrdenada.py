from claseNodo import nodo

class listaE:
    __cabeza: nodo
    __cant: int

    def __init__(self):
        self.__cabeza = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, x):
        nuevoNodo = nodo(x)
        if self.vacia():
            self.__cabeza = nuevoNodo
        else:
            actual = self.__cabeza
            anterior = None
            while actual is not None and actual.getObjeto() < x:
                anterior = actual
                actual = actual.getSiguiente()
            if anterior is None:
                nuevoNodo.setSiguiente(self.__cabeza)
                self.__cabeza = nuevoNodo
            else:
                nuevoNodo.setSiguiente(actual)
                anterior.setSiguiente(nuevoNodo)
        self.__cant += 1
        return x
    
    def suprimir(self, p):
        if self.__cant == 0:
            raise Exception("Lista vacía")
        elif p == 0:
            elemento = self.__cabeza
            self.__cabeza = self.__cabeza.getSiguiente()
            self.__cant -= 1
            return elemento.getObjeto()
        elif p < self.__cant:
            i = 0
            actual = self.__cabeza
            anterior = None
            while i < p:
                anterior = actual
                actual = actual.getSiguiente()
                i += 1
            anterior.setSiguiente(actual.getSiguiente())
            self.__cant -= 1
            return actual.getObjeto()
        else:
            raise Exception("Posición fuera de rango")
        
    def recuperar(self, p):
        if self.__cant == 0:
            raise Exception("Lista vacía")
        else:
            actual = self.__cabeza
            i = 0
            while i < p-1:
                actual = actual.getSiguiente()
                i += 1
            return actual.getObjeto()   
        
    def buscar(self, x):
        if self.__cant == 0:
            raise Exception("Lista vacía")
        else:
            i = 0
            actual = self.__cabeza
            while actual is not None:
                if actual.getObjeto() == x:
                    return i
                actual = actual.getSiguiente()
                i += 1
            raise Exception("Elemento no encontrado")
            
    def primerElemento(self):
        if self.__cant == 0:
            raise Exception("Lista vacía")
        else:
            return self.__cabeza.getObjeto()
        
    def ultimoElemento(self):
        if self.__cant == 0:
            raise Exception("Lista vacía")
        else:
            actual = self.__cabeza
            while actual.getSiguiente() is not None:
                actual = actual.getSiguiente()
            return actual.getObjeto()
        
    def anterior(self, p):
        if p <= 0 or p >= self.__cant:
            raise Exception("Posición fuera de rango")
        else:
            return p-1
    
    def siguiente(self, p):
        if p < 0 or p >= self.__cant-1:
            raise Exception("Posición fuera de rango")
        else:
            return p + 1
        
    def mostrar(self):
        if self.__cant == 0:
            raise Exception("Lista vacía")
        else:
            actual = self.__cabeza
            while actual is not None:
                print(actual.getObjeto(), end=" ")
                actual = actual.getSiguiente()
            print()

    def getCant(self):
        return self.__cant