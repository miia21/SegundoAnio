from claseObjeto import objeto
import numpy as np
import csv

class gestorObjeto:
    __arreglo: np.ndarray
    def __init__(self):
        self.__arreglo=np.array([],dtype=objeto)
    def cargar(self):       #Carga con archivo csv
        with open('G:\\Otros ordenadores\\Escritorio\\facuu\\2do año\\codigos\\practica mal\\MovimientosAbril2024.csv') as archivo:
            leer=csv.reader(archivo,delimiter=';')
            next(leer)
            for fila in leer:
                num=fila[0]
                fecha=fila[1]
                des=fila[2]
                tipo=fila[3]
                imp=float(fila[4])
                o=objeto(num, fecha, des, tipo, imp)
                self.__arreglo=np.append(self.__arreglo, o)
    def buscarNum(self, num):       #Busqueda de objeto por atributo
        cont=0
        for i in range(len(self.__arreglo)):
            if self.__arreglo[i].getNum()==num:
                cont=+1
        return cont
    def ordenar(self):      #Ordenamiento con sobrecarga de operadores
        self.__arreglo.sort()
        print("\nLa lista se ordeno con exito")
        for i in range(len(self.__arreglo)):
           print("------")
           self.__arreglo[i].mostrar()

#Arreglos numpy con incremento y busquedas con while

class gestorObjeto:
    __arreglo: np.ndarray
    __dimension=int
    __cantidad=int
    __incremento=int
    def __init__(self):
        self.__dimension=11
        self.__cantidad=0
        self.__incremento=5         #Tiene que ser multipo de la cantidad de elementos en el csv
        self.__arreglo=np.empty(self.__dimension,dtype=objeto)
    def agregarCab(self, obj):      #Agregar elementos al arrreglo
        if self.__cantidad == self.__dimension:
            self.__dimension+=self.__incremento
            nuevoArreglo = np.zeros(self.__dimension, dtype=objeto)
            nuevoArreglo[:self.__cantidad] = self.__arreglo
            self.__arreglo = nuevoArreglo
        self.__arreglo[self.__cantidad] = obj
        self.__cantidad += 1
    def cargar(self):       #Carga con archivo csv
        with open('G:\\Otros ordenadores\\Escritorio\\facuu\\2do año\\codigos\\Unidad 2\\RECUPERATORIO1\\Cabañas.csv') as archivo:
            leer=csv.reader(archivo,delimiter=';')
            for fila in leer:
                o=objeto(int(fila[0]), int(fila[1]), int(fila[2]), int(fila[3]), float(fila[4]))
                self.agregarCab(o)
            archivo.close()
    def burcarcab(self, a):     #Busqueda de elementos por atributo
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
    def buscarImp(self, num):       #Busqueda de atributo de un elemento
        i=0
        while i<len(self.__arreglo):
            if self.__arreglo[i].getNum()==num:
                x=self.__arreglo[i].getImp()
            i=i+1
        return x