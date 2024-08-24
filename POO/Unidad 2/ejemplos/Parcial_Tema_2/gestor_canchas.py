import numpy as np
import csv
from clase_cancha import cancha
class gestor_can:
    __lista:np.ndarray
    def __init__(self):
        self.__lista=np.zeros(6,dtype=object)
        self.recuperar()
    def recuperar(self):
        with open('Canchas.csv','r',newline='') as archivo:
            reader=csv.reader(archivo,delimiter=';')
            next(reader)
            i=0
            for fila in reader:
                self.__lista[i]=cancha(*fila)
                i+=1
    def importe_hora(self,id):
        i=0
        while id!=self.__lista[i].get_id():
            i+=1
        return self.__lista[i].get_imp()