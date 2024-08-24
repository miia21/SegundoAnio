from ClaseNodo import nodo

class Pila:
    pr: nodo
    ul: nodo
    cant: int
    siguiente: nodo
    def __init__(self, cant=0):
        self.__pr = None
        self.__ul = None
        self.__cant =10
        self.__siguiente = None
    def vacio(self):
        return self.__cant == 0
    def insertar(self,dato):
        nuevo = nodo(dato)
        nuevo.setSiguiente(self.__ul)
        if (self.__ul == None):
            self.__pr = nuevo
        else:
            self.__ul.setSiguiente(nuevo)
            self.__ul = nuevo
            self.__cant += 1
        return nuevo.getDato()
    def suprimir(self):
        if self.vacio():
            raise Exception("La cola esta vacia")
        else:
            aux = self.__pr
            x = self.__pr.getDato()
            self.__pr = self.__pr.getSiguiente()
            self.__cant -= 1
            return x
    def recuperar(self):
        return self.__pr.getDato()
    def recorrer(self):
        if self.vacio():
            raise Exception("La cola esta vacia")
        else:
            aux = self.__pr
            while aux != None:
                print(aux.getDato())
                aux = aux.getSiguiente()

if __name__ == "__main__":
    cola = Pila()
    cola.insertar(1)
    cola.insertar(2)
    cola.insertar(3)
    cola.recorrer()
    print("Suprime")
    cola.suprimir()
    print("Recorre")
    cola.recorrer()