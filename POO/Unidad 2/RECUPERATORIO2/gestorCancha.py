from claseCanchas import cancha
import numpy as np
import csv

class gestorCancha:
    __arreglo: np.ndarray
    __dimension=int
    __cantidad=int
    __incremento=int
    def __init__(self):
        self.__dimension=11
        self.__cantidad=0
        self.__incremento=3
        self.__arreglo=np.empty(self.__dimension,dtype=cancha)
    def agregarCancha(self, unacancha):
        if self.__cantidad == self.__dimension:
            self.__dimension+=self.__incremento
            new_arreglo = np.zeros(self.__dimension, dtype=cancha)
            new_arreglo[:self.__cantidad] = self.__arreglo
            self.__arreglo = new_arreglo
        self.__arreglo[self.__cantidad] = unacancha
        self.__cantidad += 1
    def cargar(self):
        with open('C:\\Users\\admin\\Desktop\\facuu\\2do año\\codigos\\Unidad 2\\RECUPERATORIO2\\Canchas.csv') as archivo:
            leer=csv.reader(archivo,delimiter=';')
            for fila in leer:
                can=cancha(fila[0], fila[1], float(fila[2]))
                self.agregarCancha(can)
        archivo.close()
    def buscarImp(self, num):
        i=0
        while i<len(self.__arreglo):
            if self.__arreglo[i].getId()==num:
                return self.__arreglo[i].getImp()
            i=i+1