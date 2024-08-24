from clasePedido import pedido
import csv

class gestorP:
    __lista: list
    def __init__(self):
        self.__lista=[]
    def cargaLista(self):
        with open ('G:\\Otros ordenadores\\Escritorio\\facuu\\2do año\\codigos\\Ej4\\pedidos.csv') as archivo:
            leer=csv.reader(archivo, delimiter=';')
            bandera=True
            for fila in leer:
                if bandera==True:
                    bandera=False
                else:
                    ped=pedido(fila[0],fila[1],fila[2],fila[3],fila[4])
                    self.__lista.append(ped)
        archivo.close()
    def mostrarLista(self):
        for pedido in self.__lista:
            pedido.mostrarDatos()

