import csv
from clasealquiler import alquiler

class gestoralquiler:
    __listaalquier=list

    def __init__(self):
        self.__listaalquier=[]

    def agregaalquiler(self,unalquiler):
        self.__listaalquier.append(unalquiler)

    def testalquiler(self):
        archivo=open('Alquiler.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            self.agregaalquiler(alquiler(fila[0],fila[1],fila[2],fila[3],int(fila[4])))
        archivo.close()

    def ordenar(self):
        self.__listaalquier=sorted(self.__listaalquier)
    
    def listado(self,gc):
        importetotal=0
        i=0
        print('Hora              Id de Cancha           Duracion Alquiler(Horas)          Importe por hora          Importe alquiler')
        while i<len(self.__listaalquier):
            j=0
            while j<gc._gestorcanchas__cantidad:
                identificador=gc._gestorcanchas__arreglocanchas[j].getidentificador()
                if(self.__listaalquier[i].getidentificador()==identificador):
                    horas=self.__listaalquier[i].getduracion()/60
                    importehora=gc._gestorcanchas__arreglocanchas[j].getimporte()*horas
                    importe=gc._gestorcanchas__arreglocanchas[j].getimporte()
                    importetotal=importetotal+importehora
                    print(self.__listaalquier[i].gethora(),':',self.__listaalquier[i].getmin(),'            ',self.__listaalquier[i].getidentificador(),'                    ',horas,'                              ',importe,'                 ',importehora)
                j+=1
            i+=1
        print('                                                                                       Total recaudado:',importetotal)

    def cantidadmin(self):
        id=str(input('Ingrese Identificador de Cancha:'))
        i=0
        Total=0
        band=False
        while i<len(self.__listaalquier):
            if(self.__listaalquier[i].getidentificador()==id):
                band=True
                Total=Total+self.__listaalquier[i].getduracion()
            i=i+1
        if band is True:
            print('La cancha ',id,'estuvo alquilada ',Total,'minutos')
        else:
            print('No se encontro el identificador de cancha ingresado....')
