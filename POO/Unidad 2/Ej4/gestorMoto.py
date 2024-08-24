from claseMoto import moto
import csv

class gestorM:
    __lista: list
    def __init__(self):
        self.__lista=[]
    def cargaLista(self):
        with open ('G:\\Otros ordenadores\\Escritorio\\facuu\\2do año\\codigos\\Ej4\\motos.csv') as archivo:
            leer=csv.reader(archivo, delimiter=';')
            bandera=True
            for fila in leer:
                if bandera==True:
                    bandera=False
                else:
                    mot=moto(fila[0],fila[1],fila[2],fila[3])
                    self.__lista.append(mot)
        archivo.close()
    def mostrarLista(self):
        for moto in self.__lista:
            moto.mostrarDatos()