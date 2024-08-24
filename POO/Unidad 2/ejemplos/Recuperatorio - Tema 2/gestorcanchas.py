from clasecancha import cancha
import csv
import numpy as np
class gestorcanchas:
    __cantidad=int
    __dimension=int
    __incremento=int
    __arreglocanchas=np.ndarray
    def __init__(self):
        self.__cantidad=0
        self.__dimension=17
        self.__incremento=5
        self.__arreglocanchas=np.empty(self.__dimension,dtype=cancha)
    
    def agregarcancha(self, unacancha):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            new_arreglo = np.zeros(self.__dimension, dtype=cancha)
            new_arreglo[:self.__cantidad] = self.__arreglocanchas
            self.__arreglocanchas = new_arreglo
        self.__arreglocanchas[self.__cantidad] = unacancha
        self.__cantidad += 1
    
    def testcanchas(self):
        archivo=open('Canchas.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            self.agregarcancha(cancha(fila[0],fila[1],float(fila[2])))
        archivo.close()

