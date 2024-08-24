from claseDePuntaje import *
import csv
from manejadorDeFederados import *
class manejadorPuntaje:
    __lista:list


    def __init__(self):
        self.__lista=[]
    
    def cargarManejadorP(self):
        puntaje_csv=open("evaluacion.csv",encoding='utf-8')
        reader=csv.reader(puntaje_csv,delimiter=',')
        for fila in reader:
            dni=int(fila[0])
            estilo=fila[1]
            puntaje1=float(fila[2])
            puntaje2=float(fila[3])
            puntaje3=float(fila[4])
            puntaje=clasePuntaje(dni,estilo,puntaje1,puntaje2,puntaje3)
            self.__lista.append(puntaje)
    
    def mostrarManejadorP(self):
        for puntaje in self.__lista:
            print(puntaje)
    
    def puntoA():
        federado=claseFederados()
        print(federado[0])
    

                    