from claseAlquiler import alquiler
import csv

class gestorAlquiler:
    __lista: list
    def __init__(self):
        self.__lista=[]
    def carga(self):
        with open('C:\\Users\\admin\\Desktop\\facuu\\2do año\\codigos\\Unidad 2\\RECUPERATORIO2\\Alquiler.csv') as archivo:
            leer=csv.reader(archivo, delimiter=';')
            for fila in leer:
                al=alquiler(fila[0], fila[1], fila[2], fila[3], int(fila[4]))
                self.__lista.append(al)
        archivo.close()
    def listado(self, a):
        sum=0
        self.__lista=sorted(self.__lista)
        print("Hora    Id de Cancha   Duracion alquiler  Importe por hora   Importe alquiler\n")
        for i in range(len(self.__lista)):
            horas=self.__lista[i].getDuracion()/60
            imp=a.buscarImp(self.__lista[i].getId())
            total=horas*imp
            print(f"{self.__lista[i].getHora()}:{self.__lista[i].getMin()}         {self.__lista[i].getId()}             {horas}                 {imp}              {total}\n")
            sum=sum+total
        print(f"Total recaudado: {sum}")
    def cancha(self):
        can=input("Ingrese el id de una cancha\n")
        i=0
        sum=0
        while i<len(self.__lista):
            if self.__lista[i].getId()==can:
                sum=sum+self.__lista[i].getDuracion()
            i=i+1
        print(f"La cancha {can} ha sido alquilada por: {sum} minutos\n")