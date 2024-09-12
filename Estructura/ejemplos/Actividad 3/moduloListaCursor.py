from moduloNodoCursor import NodoCursor
import numpy as np

class ListaCursor:
   __lista : np.ndarray
   __cabeza : int
   __libre : int
   __cantidad : int
   
   def __init__(self, tope : int):
      self.__lista = np.empty(tope, dtype=ListaCursor)
      self.__cabeza = 0
      self.__libre = 0
      self.__cantidad = 0
      self.inicializar()
   
   def inicializar(self) -> None:
      for i in range(len(self.__lista)):
         self.__lista[i] = NodoCursor(None)
   
   def agregar(self, dato : object):
      if self.__cantidad == 0:
         self.__lista[self.__libre].setDato(dato)
         self.__lista[self.__libre].setSiguiente(-1)
         self.__cabeza = self.__libre
      elif self.__cantidad < len(self.__lista) and self.__libre != -1:
         actual = self.__cabeza
         while self.__lista[actual].getDato() <= dato:
            actual = self.__lista[actual].getSiguiente()
         self.__lista[self.__libre].setDato(dato)
         self.__lista[self.__libre].setSiguiente(actual)
         self.__lista[actual].setSiguiente(self.__libre)
         self.__cantidad += 1
         self.__libre = self.__lista[self.__libre].getSiguiente()
      else:
         raise Exception("Lista llena")