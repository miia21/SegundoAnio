from claseMovivmiento import movimiento
import numpy as np
import csv

class gestorMovimiento:
    __movimientos: np.ndarray
    def __init__(self):
        self.__movimientos=np.array([],dtype=movimiento)
    def cargar(self):
        with open('G:\\Otros ordenadores\\Escritorio\\facuu\\2do año\\codigos\\practica mal\\MovimientosAbril2024.csv') as archivo:
            leer=csv.reader(archivo,delimiter=';')
            next(leer)
            for fila in leer:
                num=fila[0]
                fecha=fila[1]
                des=fila[2]
                tipo=fila[3]
                imp=float(fila[4])
                mov=movimiento(num, fecha, des, tipo, imp)
                self.__movimientos=np.append(self.__movimientos, mov)
    def buscarMov(self, num):
        acum=0
        print("Movimientos\nFecha              Descripcion             Importe             Tipo de Movimiento")
        for i in range(len(self.__movimientos)):
            if self.__movimientos[i].getNum()==num:
                print(f"{self.__movimientos[i].getFecha()}         {self.__movimientos[i].getDes()}          {self.__movimientos[i].getImp()}                        {self.__movimientos[i].getTipo()}")
                if self.__movimientos[i].getTipo()=='P':
                    acum=acum-self.__movimientos[i].getImp()
                else:
                    acum=acum+self.__movimientos[i].getImp()
        return float(acum)
    def buscarNum(self, num):
        cont=0
        for i in range(len(self.__movimientos)):
            if self.__movimientos[i].getNum()==num:
                cont=+1
        return cont
    def ordenar(self):
        self.__movimientos.sort()
        print("\nLa lista se ordeno con exito")
        for i in range(len(self.__movimientos)):
           print("------")
           self.__movimientos[i].mostrar()
