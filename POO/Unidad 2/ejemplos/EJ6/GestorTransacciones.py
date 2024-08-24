from claseTransacciones import transaccion
import numpy as np
import csv
class controlaT:
    __transaccion=np.ndarray 
    def __init__(self):
        self.__transaccion=np.array([], dtype=transaccion)
    def test(self):
        archivo=open('G:\\Otros ordenadores\\Mi portátil\\POO\\U2\\EJ6\\transaccionesBilletera.csv')
        lector=csv.reader(archivo,delimiter=';')
        next(lector)
        for fila in lector:
            cvu=int(fila[0])
            num=int(fila[1])
            importe=float(fila[2])
            tipo=fila[3]
            unaT=transaccion(cvu,num,importe,tipo)
            self.__transaccion=np.append(self.__transaccion,unaT)
    def modisaldo(self, cvu):
        nuevoS=0
        for i in range (len(self.__transaccion)):
            if(cvu==self.__transaccion[i].getcvu()):
                nuevoS+=self.__transaccion[i].getimporte()
        return nuevoS