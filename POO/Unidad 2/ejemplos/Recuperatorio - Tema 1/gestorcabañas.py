from clasecabaña import cabaña
import csv
import numpy as np
class gestorcabañas:
    __dimension=int
    __cantidad=int
    __incremento=int
    __arreglocabaña=np.ndarray

    def __init__(self):
        self.__dimension=11
        self.__cantidad=0
        self.__incremento=5
        self.__arreglocabaña=np.empty(self.__dimension,dtype=cabaña)
    
    def agregarcabaña(self,unacabaña):
        if self.__cantidad == self.__dimension:
            self.__dimension+=self.__incremento
            new_arreglo = np.zeros(self.__dimension, dtype=cabaña)
            new_arreglo[:self.__cantidad] = self.__arreglocabaña
            self.__arreglocabaña = new_arreglo
        self.__arreglocabaña[self.__cantidad] = unacabaña
        self.__cantidad += 1

    def testcabañas(self):
        archivo=open('Cabañas.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            self.agregarcabaña(cabaña(fila[0],int(fila[1]),int(fila[2]),int(fila[3]),fila[4]))
        archivo.close()
    
    def mostrardisponibilidad(self,gr):
        canthuesp=int(input('Ingrese cantidad de huespedes:'))
        i=0
        while i<len(self.__arreglocabaña):
            capcabaña=int((self.__arreglocabaña[i].getcantcamg()*2)+(self.__arreglocabaña[i].getcantcamc()))   
            if (capcabaña>=canthuesp and gr.notreserva(self.__arreglocabaña[i].getnumero())is False):
                print('Cabaña Disponible:',self.__arreglocabaña[i].getnumero(),'Capacidad:',capcabaña,'personas')
            i=i+1

    def importediario(self,nro):
        i=0
        while i<len(self.__arreglocabaña):
            if (nro==self.__arreglocabaña[i].getnumero()):
                importediario=self.__arreglocabaña[i].getimporte()
            i=i+1
        return importediario