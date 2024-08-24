from claseCab import cab
import numpy as np
import csv

class gestorCabana:
    __arreglo: np.ndarray
    __dimension=int
    __cantidad=int
    __incremento=int
    def __init__(self):
        self.__dimension=11
        self.__cantidad=0
        self.__incremento=5
        self.__arreglo=np.empty(self.__dimension,dtype=cab)
    def agregarCab(self, unacab):
        if self.__cantidad == self.__dimension:
            self.__dimension+=self.__incremento
            new_arreglo = np.zeros(self.__dimension, dtype=cab)
            new_arreglo[:self.__cantidad] = self.__arreglo
            self.__arreglo = new_arreglo
        self.__arreglo[self.__cantidad] = unacab
        self.__cantidad += 1
    def cargar(self):
        with open('G:\\Otros ordenadores\\Escritorio\\facuu\\2do año\\codigos\\Unidad 2\\RECUPERATORIO1\\Cabañas.csv') as archivo:
            leer=csv.reader(archivo,delimiter=';')
            for fila in leer:
                cab1=cab(int(fila[0]), int(fila[1]), int(fila[2]), int(fila[3]), float(fila[4]))
                self.agregarCab(cab1)
            archivo.close()
    def burcarcab(self, a):
        cap=int(input("Ingrese la cantidad de huespedes\n"))
        i=0
        band=False
        while i<len(self.__arreglo):
            if self.__arreglo[i]>=cap and a.buscarReserva(self.__arreglo[i].getNum())==False:
                print(f"Cabaña numero {self.__arreglo[i].getNum()} disponible\n")
                band=True
            i=i+1
        if band==False:
            print("No hay cabañas disponibles\n")
    def buscarImp(self, num):
        i=0
        while i<len(self.__arreglo):
            if self.__arreglo[i].getNum()==num:
                x=self.__arreglo[i].getImp()
            i=i+1
        return x
