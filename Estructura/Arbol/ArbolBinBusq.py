from claseNodo import nodo
from graphviz import Digraph
import time

class arbolBinBusq:
    __raiz: nodo

    def __init__(self):
        self.__raiz=None

    def getRaiz(self):
        return self.__raiz

    def insertar(self, x):
        nuevoNodo=nodo(x)
        if self.__raiz==None:
            self.__raiz=nuevoNodo
        else:
            aux=self.__raiz
            padre=None
            while aux!=None:
                padre=aux
                if x>aux.getObjeto():
                    aux=aux.getDerecha()
                else:
                    aux=aux.getIzquierda()
            if x==padre.getObjeto():
                padre.setCant(padre.getCant()+1)
            elif x>padre.getObjeto():
                padre.setDerecha(nuevoNodo)
            else:
                padre.setIzquierda(nuevoNodo)

    def suprimir(self, x):
        aux=self.__raiz
        padre=None
        while aux!=None:               ##busca el nodo a eliminar
            if x==aux.getObjeto():
                break
            padre=aux
            if x>aux.getObjeto():
                aux=aux.getDerecha()
            else:
                aux=aux.getIzquierda()
        if aux==None:                   ##si no lo encuentra
            return
        if aux.getDerecha()==None and aux.getIzquierda()==None:     ##si es hoja
            if padre==None:
                self.__raiz=None
            else:  
                if x>padre.getObjeto():
                    padre.setDerecha(None)
                else:
                    padre.setIzquierda(None)
        elif aux.getDerecha()==None or aux.getIzquierda()==None:        ##si tiene un hijo
            if aux.getDerecha()==None:          
                hijo=aux.getIzquierda()
            else:
                hijo=aux.getDerecha()
            if padre==None:
                self.__raiz=hijo
            else:
                if x>padre.getObjeto():
                    padre.setDerecha(hijo)
                else:
                    padre.setIzquierda(hijo)
        else:                                   ##si tiene dos hijos
            padre=aux
            sucesor=aux.getDerecha()
            while sucesor.getIzquierda()!=None:
                padre=sucesor
                sucesor=sucesor.getIzquierda()
            aux.setObjeto(sucesor.getObjeto())
            if padre.getObjeto()==aux.getObjeto():
                padre.setDerecha(sucesor.getDerecha())
            else:
                padre.setIzquierda(sucesor.getDerecha())

    def busqueda(self, x):
        aux = self.__raiz
        while aux is not None:
            if x == aux.getObjeto():
                return aux
            elif x > aux.getObjeto():
                aux = aux.getDerecha()
            else:
                aux = aux.getIzquierda()
        print('No se encontro el elemento')
        return None

    def altura(self, aux):
        if aux==None:
            return 0
        else:
            return 1+max(self.altura(aux.getIzquierda()), self.altura(aux.getDerecha()))
        
    def nivel(self, x):
        if self.__raiz==None:
            print('El arbol esta vacio')
        else:
            aux=self.__raiz
            nivel=0
            while aux!=None:
                if x==aux.getObjeto():
                    return nivel
                nivel+=1
                if x>aux.getObjeto():
                    aux=aux.getDerecha()
                else:
                    aux=aux.getIzquierda()
            return -1
    
    def hojas(self, aux):
        if aux is None:
            return []
        if aux.getIzquierda() is None and aux.getDerecha() is None:
            return [aux.getObjeto()]
        else:
            return self.hojas(aux.getIzquierda()) + self.hojas(aux.getDerecha())
        
    def hijo(self, auxHijo, auxPadre):
        if self.__raiz==None:
            print('El arbol esta vacio')
        else:
            x=False
            if auxPadre.getIzquierda()==auxHijo or auxPadre.getDerecha()==auxHijo:
                x=True
                return x
            else:
                return x
            
    def padre(self, auxPadre, auxHijo):
        return self.hijo(auxHijo, auxPadre)
        
    def camino(self, x, y):
        if self.__raiz is None:
            print('El arbol esta vacio')
            return []
        else:
            aux = self.busqueda(x)
            camino = []
            while aux is not None:
                camino.append(aux.getObjeto())
                if aux.getObjeto() == y:
                    return camino
                aux = aux.getDerecha() if y > aux.getObjeto() else aux.getIzquierda()
            print('No se encontro el elemento')
            return []

    def inorden(self, aux):
        if aux!=None:
            self.inorden(aux.getIzquierda())
            print(aux.getObjeto(), end=' ')
            self.inorden(aux.getDerecha())

    def preorden(self, aux):
        if aux!=None:
            print(aux.getObjeto(), end=' ')
            self.preorden(aux.getIzquierda())
            self.preorden(aux.getDerecha())

    def postorden(self, aux):
        if aux!=None:
            self.postorden(aux.getIzquierda())
            self.postorden(aux.getDerecha())
            print(aux.getObjeto(), end=' ')

    def visualizar(self):
        dot = Digraph() # crea el objeto
        self.__visualizar(dot, self.__raiz) # llama la funcion recursiva
        filename = f'arbol-{time.time()}' # crea un nombre unico para cada imagen
        dot.render(filename, format='png', cleanup=True)  # Guarda el gráfico como 'arbol.png'
       

    def __visualizar(self, dot, nodo):
      if nodo is not None:
         label = f'{nodo.getObjeto()}' # crea el string para el nodo
         dot.node(str(nodo.getObjeto()), label, shape='circle') # crea el nodo con su ID y etiqueta
         if nodo.getIzquierda() is not None:
               dot.edge(str(nodo.getObjeto()), str(nodo.getIzquierda().getObjeto()))
               self.__visualizar(dot, nodo.getIzquierda())
         if nodo.getDerecha() is not None:
               dot.edge(str(nodo.getObjeto()), str(nodo.getDerecha().getObjeto()))
               self.__visualizar(dot, nodo.getDerecha())