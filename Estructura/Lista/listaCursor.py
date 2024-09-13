from claseNodoCursor import nodoCursor
import numpy as np

class listaC:
    __max: int
    __cabeza: int
    __cant: int
    __disp: int
    __espacio: np.ndarray

    def __init__(self, xmax=10):
        self.__max = xmax
        self.__cabeza = -1  # Iniciamos con cabeza en -1 (lista vacía)
        self.__cant = 0
        self.__disp = 0
        self.__espacio = np.empty(xmax, dtype=nodoCursor)
        self.inicializa()

    def inicializa(self):
        for i in range(self.__max-1):
            self.__espacio[i] = nodoCursor(None, i+1)  # Espacio enlazado
        self.__espacio[self.__max-1] = nodoCursor(None, -1)  # Último apunta a -1 (fin de lista)
            
    def vacia(self):
        return self.__cant == 0
    
    def lleno(self):
        return self.__cant >= self.__max

    def getDisp(self):
        if self.__disp != -1:  # Si hay espacio disponible
            i = self.__disp
            self.__disp = self.__espacio[self.__disp].getSiguiente()  # Actualizamos el puntero de espacio disponible
            return i
        return -1  # No hay espacio disponible
    
    def freeDisponible(self, indice):
        if 0 <= indice < self.__max:
            self.__espacio[indice].setSiguiente(self.__disp)
            self.__disp = indice
    
    def insertarPosicion(self, x, p):
        if not (0 <= p <= self.__cant) or self.lleno():  # Verificamos límites y si hay espacio
            print("Posición incorrecta o espacio lleno.")
            return False
        
        nuevo = self.getDisp()  # Obtener índice disponible
        if nuevo == -1:
            print("No hay espacio disponible.")
            return False
        
        self.__espacio[nuevo].setObjeto(x)
        
        if p == 0:  # Insertar en la cabeza
            self.__espacio[nuevo].setSiguiente(self.__cabeza)
            self.__cabeza = nuevo
        else:
            ant = self.__cabeza
            for i in range(p - 1):  # Buscar el nodo anterior
                ant = self.__espacio[ant].getSiguiente()
            self.__espacio[nuevo].setSiguiente(self.__espacio[ant].getSiguiente())
            self.__espacio[ant].setSiguiente(nuevo)
        
        self.__cant += 1
        return True

    def insertarContenido(self, x):
        if self.lleno():
            print("Espacio lleno.")
            return False
        
        nuevo = self.getDisp()
        if nuevo == -1:
            print("No hay espacio disponible.")
            return False
        
        self.__espacio[nuevo].setObjeto(x)
        
        if self.__cabeza == -1 or self.__espacio[self.__cabeza].getObjeto() >= x:  # Insertar al inicio
            self.__espacio[nuevo].setSiguiente(self.__cabeza)
            self.__cabeza = nuevo
        else:
            ant = self.__cabeza
            cabeza = self.__cabeza
            while cabeza != -1 and self.__espacio[cabeza].getObjeto() < x:
                ant = cabeza
                cabeza = self.__espacio[cabeza].getSiguiente()
            
            self.__espacio[nuevo].setSiguiente(cabeza)
            self.__espacio[ant].setSiguiente(nuevo)
        
        self.__cant += 1
        return True
    
    def suprimir(self, p):
        if self.__cant == 0 or not (0 <= p < self.__cant):
            print("Posición incorrecta o no hay elementos.")
            return False
        
        if p == 0:  # Eliminar en la cabeza
            suprimido = self.__cabeza
            self.__cabeza = self.__espacio[suprimido].getSiguiente()
        else:
            ant = self.__cabeza
            for i in range(p - 1):  # Buscar el nodo anterior
                ant = self.__espacio[ant].getSiguiente()
            suprimido = self.__espacio[ant].getSiguiente()
            self.__espacio[ant].setSiguiente(self.__espacio[suprimido].getSiguiente())
        
        objeto_eliminado = self.__espacio[suprimido].getObjeto()
        self.freeDisponible(suprimido)
        self.__cant -= 1
        return objeto_eliminado

    def recuperar(self, p):
        if self.__cant == 0 or not (0 <= p < self.__cant):
            print("Posición incorrecta o no hay elementos.")
            return None
        
        cabeza = self.__cabeza
        for i in range(p):
            cabeza = self.__espacio[cabeza].getSiguiente()
        return self.__espacio[cabeza].getObjeto()

    def buscar(self, x):
        cabeza = self.__cabeza
        i = 0
        while cabeza != -1 and self.__espacio[cabeza].getObjeto() != x:
            cabeza = self.__espacio[cabeza].getSiguiente()
            i += 1
        if cabeza == -1:
            print("Elemento no encontrado.")
            return None
        return i

    def primerElemento(self):
        if self.vacia():
            print("Lista vacía.")
            return None
        return self.__espacio[self.__cabeza].getObjeto()

    def ultimoElemento(self):
        if self.vacia():
            print("Lista vacía.")
            return None
        cabeza = self.__cabeza
        while self.__espacio[cabeza].getSiguiente() != -1:
            cabeza = self.__espacio[cabeza].getSiguiente()
        return self.__espacio[cabeza].getObjeto()

    def sigPosicion(self, p):
        if not (0 <= p < self.__cant - 1):
            print("Posición incorrecta o no hay elementos.")
            return None
        return p + 1

    def antPosicion(self, p):
        if not (0 <= p < self.__cant):
            print("Posición incorrecta o no hay elementos.")
            return None
        return p - 1
    
    def recorrer(self):
        if self.vacia():
            print("Lista vacía.")
            return
        cabeza = self.__cabeza
        while cabeza != -1:
            print(self.__espacio[cabeza].getObjeto())
            cabeza = self.__espacio[cabeza].getSiguiente()
