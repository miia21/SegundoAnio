class Nodo:
    __objeto: object
    __siguiente: int

    def __init__(self):
        self.__objeto = None
        self.__siguiente = -2

    def setObjeto(self, x):
        self.__objeto = x

    def getObjeto(self):
        return self.__objeto

    def setSiguiente(self, xp):
        self.__siguiente = xp

    def getSiguiente(self):
        return self.__siguiente

class Lista:
    def __init__(self, xmax):
        self.__max = xmax
        self.__cabeza = 0
        self.__cantidad = 0
        self.__espacio = [Nodo() for _ in range(self.__max)]
        self.__disponible = 0

    def vacia(self):
        return self.__cantidad == 0

    def getDisponible(self):
        i = 0
        while i < self.__max and self.__espacio[i].getSiguiente() != -2:
            i += 1
        if i < self.__max:
            self.__disponible = i
            return True
        else:
            self.__disponible = -2
            return False

    def __free_disponible(self, disp):
        if 0 <= disp < self.__max:
            self.__espacio[disp].setSiguiente(-2)
            return True
        return False

    def insertar(self, x, xp):
        if (self.__cantidad < self.__max) and (0 <= xp <= self.__cantidad) and self.getDisponible():
            self.__espacio[self.__disponible].setObjeto(x)
            ant = self.__cabeza
            cabeza = self.__cabeza
            i = 0
            while i < xp:
                i += 1
                ant = cabeza
                cabeza = self.__espacio[cabeza].getSiguiente()
            if cabeza == self.__cabeza:  # inserta al inicio
                if self.__cantidad == 0:  # lista vacía
                    self.__espacio[self.__cabeza].setSiguiente(-1)
                else:  # lista con elementos
                    self.__espacio[self.__disponible].setSiguiente(self.__cabeza)
                self.__cabeza = self.__disponible
            elif cabeza == -1:  # inserta al final
                self.__espacio[self.__disponible].setSiguiente(-1)
                self.__espacio[ant].setSiguiente(self.__disponible)
            else:
                self.__espacio[self.__disponible].setSiguiente(cabeza)
                self.__espacio[ant].setSiguiente(self.__disponible)
            self.__cantidad += 1
            return True
        else:
            print("Espacio lleno o posición incorrecta.")
            return False
        
    def insertarContenido(self, x):
        if (self.__cantidad < self.__max) and self.getDisponible():
            ant = self.__cabeza
            cabeza = self.__cabeza
            i = 0
            self.__espacio[self.__disponible].setObjeto(x)
            while (i < self.__cantidad) and (cabeza != -1) and (self.__espacio[cabeza].getObjeto() < x):
                i += 1
                ant = cabeza
                cabeza = self.__espacio[cabeza].getSiguiente()
            if cabeza == self.__cabeza:    #inicio
                if self.__cantidad == 0:  # lista vacía
                    self.__espacio[self.__cabeza].setSiguiente(-1)
                else:  # lista con elementos
                    self.__espacio[self.__disponible].setSiguiente(self.__cabeza)
                self.__cabeza = self.__disponible
            elif cabeza == -1:         #final
                self.__espacio[self.__disponible].setSiguiente(-1)
                self.__espacio[ant].setSiguiente(self.__disponible)
            else:                      #medio   
                self.__espacio[self.__disponible].setSiguiente(cabeza)
                self.__espacio[ant].setSiguiente(self.__disponible)
            self.__cantidad += 1
            return True
        else:
            print("Espacio lleno.")
            return False

    def suprimir(self, xp):
        if (self.__cantidad != 0) and (0 <= xp < self.__cantidad):
            ant = self.__cabeza
            cabeza = self.__cabeza
            i = 0
            while i < xp and cabeza != -1:
                i += 1
                ant = cabeza
                cabeza = self.__espacio[cabeza].getSiguiente()
            if cabeza == self.__cabeza:
                if self.__cantidad == 1:
                    self.__cabeza = 0
                else:
                    self.__cabeza = self.__espacio[ant].getSiguiente()
            else:
                self.__espacio[ant].setSiguiente(self.__espacio[cabeza].getSiguiente())
            x = self.__espacio[cabeza].getObjetosetObjeto()
            self.__disponible = cabeza
            self.__free_disponible(self.__disponible)
            self.__cantidad -= 1
            return x
        else:
            print("Lista vacía o posición incorrecta.")
            return None

    def recuperar(self, xp):
        if (self.__cantidad != 0) and (0 <= xp < self.__cantidad):
            cabeza = self.__cabeza
            i = 0
            while cabeza != -1 and i < xp:
                i += 1
                cabeza = self.__espacio[cabeza].getSiguiente()
            return self.__espacio[cabeza].getObjetosetObjeto()
        else:
            print("Lista vacía o posición incorrecta.")
            return None

    def recorrer(self):
        if self.__cantidad != 0:
            cabeza = self.__cabeza
            print("Lista:", end=" ")
            while cabeza != -1:
                print(self.__espacio[cabeza].getObjetosetObjeto(), end=" ")
                cabeza = self.__espacio[cabeza].getSiguiente()
            print()
        else:
            print("Lista vacía.")


if __name__ == "__main__":
    lista = Lista(10)
    lista.insertar(1, 0)
    lista.insertar(2, 1)
    lista.insertar(3, 2)
    lista.insertar(4, 3)
    lC(7)
    lC(6)
    lC(5)
    lC(8)
    lista.recorrer()
    lista.suprimir(3)
    lista.recorrer()
    print(lista.recuperar(3))

