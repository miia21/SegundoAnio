from claseDeFederados import *
import csv
class manejadorFederados:
    __lista:list
    
    def __init__(self):
        self.__lista=[]
        
    def cargarManejador(self):
        federados_csv=open("federados.csv",encoding='utf-8')
        reader=csv.reader(federados_csv,delimiter=',')
        for fila in reader:
            apellido=fila[0]
            nombre=fila[1]
            dni=int(fila[2])
            edad=int(fila[3])
            club=fila[4]
            federado=claseFederados(apellido,nombre,dni,edad,club)
            self.__lista.append(federado)
    
    def mostrarManejadorF(self):
        for federado in self.__lista:
            print(federado)
    
    