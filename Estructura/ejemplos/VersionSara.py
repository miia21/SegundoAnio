class Nodo:
    def __init__(self):
        self.dato = 0
        self.siguiente = -2  # equivale a None

    def set_dato(self, x):
        self.dato = x

    def get_dato(self):
        return self.dato

    def set_siguiente(self, xp):
        self.siguiente = xp

    def get_siguiente(self):
        return self.siguiente


class Lista:
    def __init__(self, xmax):
        self.max = xmax
        self.cab = 0
        self.cantidad = 0
        self.espacio = [Nodo() for _ in range(max)]
        self.disponible = 0

    def vacia(self):
        return self.cantidad == 0

    def get_disponible(self):
        for i in range(self.max):
            if self.espacio[i].get_siguiente() == -2:
                return i
        return -2  # No hay espacio disponible

    def free_disponible(self, disp):
        if 0 <= disp < self.max:
            self.espacio[disp].set_siguiente(-2)
            return True
        return False

    def insertar_por_posicion(self, x, xp):
        if self.cantidad < self.max and 0 <= xp <= self.cantidad:
            self.disponible = self.get_disponible()
            if self.disponible != -2:
                self.espacio[self.disponible].set_dato(x)
                ant = self.cab
                cabeza = self.cab
                for i in range(xp):
                    ant = cabeza
                    cabeza = self.espacio[cabeza].get_siguiente()

                if cabeza == self.cab:  # Inserta al inicio de la lista
                    if self.cantidad == 0:  # Inserta en la lista vacía
                        self.espacio[self.cab].set_siguiente(-1)
                    else:  # Inserta en la lista con elementos
                        self.espacio[self.disponible].set_siguiente(self.cab)
                    self.cab = self.disponible
                elif cabeza == -1:  # Inserta al final de la lista
                    self.espacio[self.disponible].set_siguiente(-1)
                    self.espacio[ant].set_siguiente(self.disponible)
                else:
                    self.espacio[self.disponible].set_siguiente(cabeza)
                    self.espacio[ant].set_siguiente(self.disponible)

                self.cantidad += 1
                return True
        print("Espacio lleno o posición incorrecta.")
        return False

    def insertar_por_contenido(self, x):
        if self.cantidad < self.max:
            self.disponible = self.get_disponible()
            if self.disponible != -2:
                ant = self.cab
                cabeza = self.cab
                i = 0
                self.espacio[self.disponible].set_dato(x)
                while i < self.cantidad and cabeza != -1 and self.espacio[cabeza].get_dato() < x:
                    i += 1
                    ant = cabeza
                    cabeza = self.espacio[cabeza].get_siguiente()

                if cabeza == self.cab:  # Inserta al inicio de la lista
                    if self.cantidad == 0:  # Inserta en la lista vacía
                        self.espacio[self.cab].set_siguiente(-1)
                    else:  # Inserta en la lista con elementos
                        self.espacio[self.disponible].set_siguiente(self.cab)
                    self.cab = self.disponible
                elif cabeza == -1:  # Inserta al final de la lista
                    self.espacio[self.disponible].set_siguiente(-1)
                    self.espacio[ant].set_siguiente(self.disponible)
                else:
                    self.espacio[self.disponible].set_siguiente(cabeza)
                    self.espacio[ant].set_siguiente(self.disponible)

                self.cantidad += 1
                return True
        print("Espacio lleno.")
        return False

    def suprimir(self, xp):
        if self.cantidad != 0 and 0 <= xp < self.cantidad:
            ant = self.cab
            cabeza = self.cab
            for i in range(xp):
                ant = cabeza
                cabeza = self.espacio[cabeza].get_siguiente()

            if cabeza == self.cab:
                if self.cantidad == 1:
                    self.cab = 0
                else:
                    self.cab = self.espacio[ant].get_siguiente()
            else:
                self.espacio[ant].set_siguiente(self.espacio[cabeza].get_siguiente())

            x = self.espacio[cabeza].get_dato()
            self.disponible = cabeza
            self.free_disponible(self.disponible)
            self.cantidad -= 1
            return x
        print("Lista vacía o posición incorrecta.")
        return None

    def recuperar(self, xp):
        if self.cantidad != 0 and 0 <= xp < self.cantidad:
            cabeza = self.cab
            for i in range(xp):
                cabeza = self.espacio[cabeza].get_siguiente()
            return self.espacio[cabeza].get_dato()
        print("Lista vacía o posición incorrecta.")
        return None

    def buscar(self, x):
        if self.cantidad != 0:
            cabeza = self.cab
            for i in range(self.cantidad):
                if cabeza != -1 and self.espacio[cabeza].get_dato() == x:
                    return i + 1
                cabeza = self.espacio[cabeza].get_siguiente()
        print("Lista vacía.")
        return 0

    def primer_elemento(self):
        if self.cantidad != 0:
            return self.espacio[self.cab].get_dato()
        print("Lista vacía.")
        return None

    def ultimo_elemento(self):
        if self.cantidad != 0:
            cabeza = self.cab
            aux = 0
            while cabeza != -1:
                aux = self.espacio[cabeza].get_dato()
                cabeza = self.espacio[cabeza].get_siguiente()
            return aux
        print("Lista vacía.")
        return None

