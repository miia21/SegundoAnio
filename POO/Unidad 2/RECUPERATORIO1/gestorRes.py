from claseRes import reserva
import csv

class gestorReserva:
    __lista: list
    def __init__(self):
        self.__lista=[]
    def cargar(self):
        with open('G:\\Otros ordenadores\\Escritorio\\facuu\\2do año\\codigos\\Unidad 2\\RECUPERATORIO1\\Reservas.csv') as archivo:
            leer=csv.reader(archivo, delimiter=';')
            for fila in leer:
                res=reserva(int(fila[0]), fila[1], int(fila[2]), fila[3], int(fila[4]), int(fila[5]), float(fila[6]))
                self.__lista.append(res)
    def buscarReserva(self, num):
        i=0
        band=False
        while i<len(self.__lista) and band==False:
            if self.__lista[i].getNumcab()==num:
                band=True
            i=i+1
        return band
    def fechas(self, a):
        f=input("Ingrese una fecha\n")
        i=0
        print("N° Cabaña  Importe diario  Cantidad de dias       Seña           Importe a cobrar\n")
        while i<len(self.__lista):
            if f==self.__lista[i].getFecha():
                imp=a.buscarImp(self.__lista[i].getNumcab())
                imp2=(self.__lista[i].getCantd()*imp)-self.__lista[i].getSena()
                print(f"    {self.__lista[i].getNumcab()}           {imp}            {self.__lista[i].getCantd()}          {self.__lista[i].getSena()}             {imp2}")
            i=i+1
